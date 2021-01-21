#!/data/data/com.termux/files/usr/bin/sh

cd /data/data/com.termux/files/home/

echo -e "\nGet the necessary components"

apt update -y

apt install -y openssh-server

echo -e "\nSetup the necessary files"

wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/SSH/Apt/sshd_config -P /etc/ssh

echo -e "\nYou can now start OpenSSH Server by running /etc/init.d/ssh start"

echo -e "\nThe Open Server will be started at 127.0.0.1:22"

termux-open 127.0.0.1:22
