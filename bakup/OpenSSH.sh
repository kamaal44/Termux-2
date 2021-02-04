#!/data/data/com.termux/files/usr/bin/sh

echo "\nOpenSSH Install"

pkg install -y openssh

apt update -y && apt upgrade -y

passwd
