#!/data/data/com.termux/files/usr/bin/sh

echo "Kick Them Out Install"

cd /sdcard/apps/

git clone https://github.com/roccomuso/kickthemout.git

cd kickthemout

npm install -g --production

echo "Cleaning up Directory"

rm -rf .git/ DOTgit .gitignore LICENSE
