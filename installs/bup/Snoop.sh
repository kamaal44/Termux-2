#!/data/data/com.termux/files/usr/bin/bash

echo "\nSnoop Install"

echo "\nSnoop Project is one of the most promising OSINT tools for finding nicknames."

termux-setup-storage

apt-get update -y

apt-get upgrade -y

pkg update -y

pkg upgrade -y

pkg install -y python

pkg install -y python

pkg install -y libcrypt

pkg install -y libxml2

pkg install -y libxslt

pkg install -y git

pkg install -y coreutils

apt-get install -y python3 python3-pip

apt-get install -y ttf-ancient-fonts

apt-get install -y fonts-noto-color-emoji

cd /sdcard/github/Termux/python/

git clone https://github.com/snooppr/snoop

cd snoop

echo "\nInstall the 'requirements' dependencies"

python3 -m pip install --upgrade pip

python3 -m pip install -r requirements.txt

python3 -m pip install module
