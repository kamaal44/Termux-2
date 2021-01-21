#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nFTP Install"

source $PREFIX/profile.d/start-services

sv-enable ftpd

sv up ftpd
