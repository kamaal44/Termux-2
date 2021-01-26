Title:
======
SimpleTransfer 2.2.1 - Command Injection Vulnerabilities


Date:
=====
2013-05-03


References:
===========
http://www.vulnerability-lab.com/get_content.php?id=937


VL-ID:
=====
937


Common Vulnerability Scoring System:
====================================
5.6


Introduction:
=============
Simple Transfer is the easiest way of transferring your Photos and Videos to computer and other iOS devices via WiFi. 
No need for cable, iTunes or extra software.

* View all your photo albums and videos on your computer and download them as zip file via WiFi
* Send multiple photos and videos from your computer to your device
* Transfer any number of photos and videos between iOS devices (iPhone, iPad and iPod Touch), 
select an album and tap on ``Select All`` to transfer all your photos/videos
* Ability to create new albums and transfer to photos/videos to other albums
* Photos are transferred with full resolution including metadata and videos transferred with the highest quality
* No limit on the number or size of the photos/videos you transfer between devices or computers
* Slideshow photo albums on your computer`s browser
* Pay only once to install the app on all your iOS devices (iPhone, iPad and iPod Touch)
* Works on Windows, Mac and Linux and it`s fast!

(Copy of the Homepage: https://itunes.apple.com/de/app/simple-transfer/id411292121 )


Abstract:
=========
The Vulnerability Laboratory Research Team discovered multiple local command injection vulnerabilities in the mobile Simple-Transfer Photo 2.2.1 iOS app (Apple - iPad|iPhone).


Report-Timeline:
================
2013-05-03:	Public Disclosure


Status:
========
Published


Affected Products:
==================
Apple AppStore
Product: SimpleTransfer Photo iOS 2.2.1


Exploitation-Technique:
=======================
Local


Severity:
=========
High


Details:
========
Multiple local command injection web vulnerabilities are detected  in the mobile SimpleTransfer Photo 2.2.1 iOS app (Apple - iPad|iPhone).
The vulnerability allows to inject local commands via vulnerable system values to compromise the apple mobile iOS application.

The first vulnerability is located in the index module when processing to load the unique ipad or iphone device name. 
Local attackers can change the ipad or iphone device name to system specific commands and file requests to provoke 
the execution when processing to watch the main index photo listing. The execution of the script code occurs in the 
header were the device name web context is located when processing to display the device name in the index listing.

The secound vulnerability is located in the index module when processing to load the ipad or iphone photo album folder names. 
Local attackers can change the ipad or iphone photo album names to system specific commands and file requests to provoke 
the execution when processing to watch the main index album listing. The execution of the script code occurs in the album 
folder name web context when processing to display the vulnerable name value listing.

Exploitation of the web vulnerability requires an application user account (standard) and low or medium user interaction.
Successful exploitation of the vulnerability results unauthorized execution of system specific commands and file or path requests.


Vulnerable Application(s):
				[+] SimpleTransfer Photo 2.2.1 - ITunes or AppStore (Apple)

Vulnerable Parameter(s):
				[+] Device Name
				[+] Album Folder/Path Name

Affected Module(s):
				[+] Index Listing - Header
				[+] Album Listing - Name


Proof of Concept:
=================
1.1	PoC: Device Name - Index

<html xmlns="http://www.w3.org/1999/xhtml"><head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=7">
        <title>iPad 360 �337%20>"<../[LOCAL COMMAND INJECTION VULNERABILITY]\'></title>
		
		<link href="index_files/jquery-ui-1.css" type="text/css" rel="stylesheet">
		<link href="index_files/default.css" rel="stylesheet" type="text/css" media="screen">
		<link href="index_files/uploadify.css" rel="stylesheet" type="text/css" media="screen">
		
		<script type="text/javascript" src="index_files/jquery-1.js"></script>
		<script type="text/javascript" src="index_files/jquery-ui-1.js"></script> 
		<script type="text/javascript" src="index_files/jquery.js"></script>

		<script type="text/javascript">

Local Device Name Command Inject: 	(http://localhost/rambax/)



1.2	PoC:  Album Name - Photo Listing

<div id="page-title">Sky Lounge%20>"../[LOCAL COMMAND INJECTION VULNERABILITY]\' src="D64E64A5-7C0B-4530-B4F5-7406D5BDF168_files/LOACAL.htm">
 <span>(4)</span></div>
                    </td>
                    <td align="right" style="width: 20%;">
						<div id="header-links">
							<ul>
								<li><a href="/" title="Home">Back to 
Albums</a></li>


Local Album Name Command Inject: 	(http://localhost:8080/rambax/album/D64E64A5-7C0B-4530-B4F5-7406D5BDF168)


Solution:
=========
The vulnerabilities can be patched by a secure parse of the album name and device name parameter.
Encode the strings and set an own exception-handling to prevent against future command injection attacks.


Risk:
=====
The security risk of the local command injection web vulnerabilities are estimated as high(-).


Credits:
========
Vulnerability Laboratory [Research Team] - Benjamin Kunz Mejri (bkm@vulnerability-lab.com) [www.vulnerability-lab.com]


Disclaimer:
===========
The information provided in this advisory is provided as it is without any warranty. Vulnerability-Lab disclaims all warranties, 
either expressed or implied, including the warranties of merchantability and capability for a particular purpose. Vulnerability-
Lab or its suppliers are not liable in any case of damage, including direct, indirect, incidental, consequential loss of business 
profits or special damages, even if Vulnerability-Lab or its suppliers have been advised of the possibility of such damages. Some 
states do not allow the exclusion or limitation of liability for consequential or incidental damages so the foregoing limitation 
may not apply. We do not approve or encourage anybody to break any vendor licenses, policies, deface websites, hack into databases 
or trade with fraud/stolen material.

Domains:    www.vulnerability-lab.com   	- www.vuln-lab.com			       - www.vulnerability-lab.com/register
Contact:    admin@vulnerability-lab.com 	- support@vulnerability-lab.com 	       - research@vulnerability-lab.com
Section:    video.vulnerability-lab.com 	- forum.vulnerability-lab.com 		       - news.vulnerability-lab.com
Social:	    twitter.com/#!/vuln_lab 		- facebook.com/VulnerabilityLab 	       - youtube.com/user/vulnerability0lab
Feeds:	    vulnerability-lab.com/rss/rss.php	- vulnerability-lab.com/rss/rss_upcoming.php   - vulnerability-lab.com/rss/rss_news.php

Any modified copy or reproduction, including partially usages, of this file requires authorization from Vulnerability Laboratory. 
Permission to electronically redistribute this alert in its unmodified form is granted. All other rights, including the use of other 
media, are reserved by Vulnerability-Lab Research Team or its suppliers. All pictures, texts, advisories, source code, videos and 
other information on this website is trademark of vulnerability-lab team & the specific authors or managers. To record, list (feed), 
modify, use or edit our material contact (admin@vulnerability-lab.com or support@vulnerability-lab.com) to get a permission.

    				   	Copyright � 2013 | Vulnerability Laboratory

-- 
VULNERABILITY RESEARCH LABORATORY
LABORATORY RESEARCH TEAM
CONTACT: research@vulnerability-lab.com