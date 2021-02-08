#!/data/data/com.termux/files/usr/bin/bash

echo "Tool-X Install"

apt update

apt install -y git

cd /sdcard/github/Termux/python/

git clone https://github.com/rajkumardusad/Tool-X.git

cd Tool-X

chmod +x install

sh install

rm -rf .git LICENSE .github/
