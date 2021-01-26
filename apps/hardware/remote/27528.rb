source: https://www.securityfocus.com/bid/17175/info

FirePass 4100 SSL VPN is prone to a cross-site scripting vulnerability. This issue is due to a failure in the application to properly sanitize user-supplied input. 

An attacker may leverage this issue to have arbitrary script code executed in the browser of an unsuspecting user in the context of the affected site. This may facilitate the theft of cookie-based authentication credentials as well as other attacks.

https://www.example.com/my.support.php3?c=1&s=username</title><img src=http://www.example.com/EXPLOIT.JS>&lang=en&charset=iso-8859-1&uilangchar=en.iso-8859-1