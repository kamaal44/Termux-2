source: https://www.securityfocus.com/bid/45688/info

Lexmark Printer X651de is prone to an HTML-injection vulnerability because it fails to properly sanitize user-supplied input before using it in dynamically generated content.

Successful exploits will allow attacker-supplied HTML and script code to run in the context of the affected printer web interface application, potentially allowing the attacker to steal cookie-based authentication credentials or to control how the site is rendered to the user. Other attacks are also possible.

Lexmark Printer X651de is vulnerable; other versions may also be affected. 

nmap --script=pjl-ready-message.nse --script-args='pjl_ready_message="<script>alert(1);</script>"'