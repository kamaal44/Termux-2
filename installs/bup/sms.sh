#!/data/data/com.termux/files/usr/bin/sh

echo "\nTermux SMS Install"

echo "\nSend text message in termux."

pkg install -y git

cd /sdcard/github/Termux/apps/

git clone https://github.com/ZechBron/Termux-SMS

cd Termux-SMS

chmod +x setup.sh

echo "\nIt is recommended to run setup.sh first`"

sh setup.sh

sh TermuxSMS.sh

rm -rf .git .gitignore
