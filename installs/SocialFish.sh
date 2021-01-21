#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nSocialFish Install"

cd /sdcard/github/Termux/python/

apt update -y

apt upgrade -y

apt install -y git

apt install -y python

apt install -y python2

git clone https://github.com/UndeadSec/SocialFish.git

cd SocialFish

chmod +x *

python3 -m pip install -r requirements.txt

echo -e "\nusage :"

python3 SocialFish.py

echo -e "\nNow select your target and it will generate an url using Ngrok"

sleep 5s

rm -rf .git .github CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE
