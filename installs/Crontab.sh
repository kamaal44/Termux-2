#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nCrontab Install"

pkg install -y cronie

pkg install -y termux-services

sv-enable crond

crontab -e

mkdir -p /data/data/com.termux/files/home/crontab-testing
