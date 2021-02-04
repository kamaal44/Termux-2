#!/data/data/com.termux/files/usr/bin/sh

echo "\nDorks Eye Install"

cd /sdcard/github/Termux/python/

git clone https://github.com/BullsEye0/dorks-eye.git

cd dorks-eye

python3 -m pip install -r requirements.txt

rm -rf .git LICENSE Img/
