#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nTBomb Install"

cd /sdcard/github/Termux/apps

pkg install -y git

pkg install -y python

git clone https://github.com/TheSpeedX/TBomb.git

cd TBomb

python3 -m pip install -r requirements.txt

chmod +x TBomb.sh

echo -e "\nCleaing Up Repo"

rm -rf .git LICENSE .gitignore

sh TBomb.sh
