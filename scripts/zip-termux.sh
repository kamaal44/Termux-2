#!/data/data/com.termux/files/usr/bin/sh

cd /sdcard/github/Termux/

echo "\n####  <--Zipping Termux Folder -->  ####\n"

zip Termux.zip Documents/ README.md Termux.png apps/ home/ installs/ links/ python/ ruby/ scripts/

mv -v Termux.zip /sdcard/Download/

echo "\n####  <-- Done -->  ####\n"
