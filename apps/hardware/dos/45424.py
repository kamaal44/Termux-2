# Exploit Title: D-Link DIR-615 - Denial of Service (PoC)
# Date: 2018-08-09
# Vendor Homepage: http://www.dlink.co.in
# Hardware Link:  https://www.amazon.in/D-Link-DIR-615-Wireless-N300-Router-Black/dp/B0085IATT6
# Version: D-Link DIR-615
# Category: Hardware
# Exploit Author:  Aniket Dinda
# Tested on: Linux (kali linux)
# Web: https://hackingvila.wordpress.com/2018/08/24/d-link-dir-615-buffer-overflow-via-a-long-authorization-http-header-click-here/
# Cve: CVE-2018-15839

# Proof Of Concept:

1- First connect to this network
2- Open BurpSuite and then start the intercept, making the necessary proxy changes to the internet browser.
3- Goto Easy setup > 
4- Now as the Burp is intercept is on, you will find an Authorization: Basic or cookie: SessionId followed by a string. Now we paste a string consisting oaf 5000 zeros.
5- Then forward the connection
6- Then your router automatically log out and the net connection will be gone.