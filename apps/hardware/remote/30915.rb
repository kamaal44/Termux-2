source: https://www.securityfocus.com/bid/26808/info

Thomson SpeedTouch 716 is prone to a cross-site scripting vulnerability because the device fails to properly sanitize user-supplied input.

An attacker may leverage this issue to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected site. This may help the attacker steal cookie-based authentication credentials and launch other attacks.

This issue affects Thomson SpeedTouch 716 firmware 6.2.17.50 and 5.4.0.14; other versions may also be affected. 

http://www.example.com/cgi/b/ic/connect/?nm=1&client=192.168.1.72&server=&event=ServerTimeout&url=<script>alert('bla');</script>