#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nMariaDB Install"

pkg install mariadb

echo -e "\nThe installation should finish without any error. If error occurred, you probably need to report the issue on Github."

echo -e "\nThe command shown above will also initialize the database with 2 all-privilege accounts (introduced perhaps in MariaDB 10.4.x). The first one is "root" which is inaccessible and the second one with name of your Termux user (check with command id -un or whoami)."

echo -e "\nTo enable access to root account, you need to login with your Termux user name"

mysql -u $(whoami)

echo -e "\nand manually change password for root"

use mysql;

set password for 'root'@'localhost' = password('$Hustle4$');

flush privileges;

quit;

echo -e "\nVerify that you are able to login as 'root' with mysql -u root -p. You will need to provide password set in previous step."

mysql -u root -p

echo -e "\nWhenever you want to access MySQL database manually through command line or with some program (web application), you need to start MySQL server:"

mysqld_safe

echo -e "\nThen you should be able to connect to database, e.g. with mysql -u root -p."

mysql -u root -p
