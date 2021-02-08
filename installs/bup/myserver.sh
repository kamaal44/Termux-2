#!/data/data/com.termux/files/usr/bin/bash

echo "MyServer Install"

cd /sdcard/github/Termux/apps/

git clone https://github.com/rajkumardusad/MyServer.git

cd MyServer

chmod +x install

sh install

find . -depth -type d -name ".git" -exec rm -rf {} \; && find . -depth -type d -name ".github" -exec rm -rf {} \;
