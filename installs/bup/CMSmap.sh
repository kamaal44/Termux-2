#!/data/data/com.termux/files/usr/bin/sh

echo "\nCMSmap Install"

cd /sdcard/github/Termux/python/

git clone https://github.com/Dionach/CMSmap.git

cd CMSmap

rm -rf .git/ .github/ .gitignore DISCLAIMER.txt LICENSE.txt

chmod +x cmsmap.py

python3 setup.py install

python3 cmsmap.py -h
