source: https://www.securityfocus.com/bid/52881/info

Peakflow SP is prone to a cross-site scripting vulnerability because it fails to sanitize user-supplied input.

An attacker may leverage this issue to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected site. This may allow the attacker to steal cookie-based authentication credentials and launch other attacks. 

https://www.example.com/index/"onmouseover="alert(666)