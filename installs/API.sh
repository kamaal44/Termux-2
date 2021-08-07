#!/data/data/com.termux/files/usr/bin/sh

echo "\nTermux API Install"

pkg install termux-api

apt update -y

apt upgrade -y

pkg update -y

pkg upgrade -y
