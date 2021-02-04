#!/data/data/com.termux/files/usr/bin/sh

echo "\n"PRoot Install"

pkg install -y proot proot-distro

cd /data/data/com.termux/files/home/

mkdir -p ./rootfs

proot -r ./rootfs -0 -w / -b /dev -b /proc -b /sys /bin/sh

proot-distro install ubuntu

proot-distro install nethunter

proot-distro install archlinux

proot-distro install alpine
