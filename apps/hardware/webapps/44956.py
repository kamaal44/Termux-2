# Exploit Title: DIGISOL DG-HR3400 Wireless Router -  Cross-Site Scripting
# Date: 2018-06-25
# Vendor Homepage:  http://www.digisol.com
# Hardware Link: https://www.amazon.in/Digisol-DG-HR3400-300Mbps-Wireless-Broadband/dp/B00IL8DR6W
# Category: Hardware
# Exploit Author: Adipta Basu
# Tested on: Mac OS High Sierra
# CVE: N/A
 
# Reproduction Steps:
 
   - Goto your Wifi Router Gateway [i.e: http://192.168.2.1]
   - Go to --> "General Setup" --> "Wireless" --> "Basic Settings"
   - Open BurpSuite
   - Change the SSID to "Testing" and hit "Apply"
   - Burp will capture the intercepts.
   - Now change the SSID to <script>alert("ADIPTA")</script> and keep APSSID as it is
   - Refresh the page, and you will get the "ADIPTA" pop-up