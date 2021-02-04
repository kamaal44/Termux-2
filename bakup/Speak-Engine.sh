#!/data/data/com.termux/files/usr/bin/sh

echo "\nTermux Speak Install"

cd /sdcard/github/Termux/apps/

git clone https://github.com/TechnicalMujeeb/Termux-speak

cd Termux-speak

chmod +x *

sh install.sh
