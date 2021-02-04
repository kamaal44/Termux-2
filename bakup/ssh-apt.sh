#!/data/data/com.termux/files/usr/bin/sh

cd /data/data/com.termux/files/home/

echo "\nGet the necessary components"

apt update -y

apt install -y openssh-server

echo "\nSetup the necessary files"

wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/SSH/Apt/sshd_config -P /etc/ssh

echo "\nYou can now start OpenSSH Server by running /etc/init.d/ssh start"

echo "\nThe Open Server will be started at 127.0.0.1:22"

termux-open 127.0.0.1:22
