# Exploit Title:- TP-Link Wireless N Router WR840N - Denial of Service (PoC)
# Date: 2018-08-05
# Vendor Homepage: https://www.tp-link.com/
# Hardware Link:  https://www.amazon.in/TP-LINK-TL-WR840N-300Mbps-Wireless-External/dp/B01A0G1J7Q
# Version: TP-Link Wireless N Router WR840N
# Category: Hardware
# Exploit Author:  Aniket Dinda
# Tested on: Windows 10
# Web: https://hackingvila.wordpress.com
# CVE: N/A

# Proof Of Concept:

1- First connect to this network.
2- Open BurpSuite and then start the intercept, making the necessary proxy changes to the internet browser.
3- Go to Quick setup. 
4- Now as the Burp is intercept is on, you will find an Authorization: Basic followed by a string. 
5- Now we paste a string consisting of 2000 zeros.
6- Then forward the connection.
7- Then your router automatically logout and net connection will be gone.

You have to reboot your router before it becomes available again.