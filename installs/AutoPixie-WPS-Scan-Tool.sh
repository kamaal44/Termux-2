#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nAutoPixie WPS Scan Tool Install"

cd /sdcard/github/Termux/python/

python3 -m pip install requests

echo -e "\nHow to use AutoPixie Wps Scan Tool in Termux"

git clone https://github.com/nxxxu/AutoPixieWps.git

cd AutoPixieWps

rm -rf .git/

chmod +x autopixie.py

python3 autopixie.py
