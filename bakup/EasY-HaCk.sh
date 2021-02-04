#!/data/data/com.termux/files/usr/bin/sh

echo "EasY-HaCk Install"

cd /data/data/com.termux/files/home

git clone https://github.com/sabri-zaki/EasY_HaCk

cd EasY_HaCk/

chmod +x install.sh

sh install.sh

find . -depth -type d -name ".git" -exec rm -rf {} \; && find . -depth -type d -name ".github" -exec rm -rf {} \;

rm -rf CONTRIBUTING.md LICENSE
