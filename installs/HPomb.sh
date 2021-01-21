#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nHPomb Install"

cd cd /sdcard/python/

pkg install git

pkg install python

git clone https://github.com/HoneyPots0/HPomb.git

cd HPomb

chmod +x hpomb.py

python3 -m pip install -r requirements.txt

rm -rf .git LICENSE
