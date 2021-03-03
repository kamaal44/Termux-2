#!/bin/sh

cd /sdcard/github/
echo "\nCloning dotfiles Repo\n"
git clone https://github.com/NateWeiler/dotfiles.git
cd /sdcard/github/dotfiles/
echo "\nRemoving old Note-Termux Folder\n"
rm -rf Note-Termux/
mkdir -p Note-Termux
mkdir -p Note-Termux/backups
touch Note-Termux/backups/.gitkeep
cd /data/data/com.termux/files/home/
echo "\nZipping Note-Termux.zip"
zip -r -q Note-Termux.zip Mail Optiva-Framework aliases apktool bin buildAPKs builtAPKs codiad crontab-testing crontab.txt data debian-testing deboot_debian debootstrap etc export files functions go kali-fs kali.sh metasploit-framework neofetch oh-my-fish pad.txt prefix progs routersploit start-kali.sh start-ubuntu.sh termux-desktop termux.properties tmp ubuntu-fs ubuntu.sh xerxes
echo "\nUnzipping Note-Termux.zip\n"
unzip -qq Note-Termux.zip -d /sdcard/github/dotfiles/Note-Termux/
echo "\nRemoving Note-Termux.zip\n"
rm -rf Note-Termux.zip
cd /sdcard/github/dotfiles/Note-Termux/
find . -depth -type d -name ".git" -exec rm -rf {} \;
find . -depth -type d -name ".github" -exec rm -rf {}
\;
find . -depth -type f -name "desktop.ini" -exec rm -rf {} \;
find . -depth -type f -name "DS_Store" -exec rm -rf {} \;
cd /sdcard/github/dotfiles/
echo "\nAdding files to Commit\n"
git add -A
echo "\nCommitting files to Repo\n"
git commit -m "Note Termux"
echo "\nPushing files to Repo with Force\n"
git push --force
git status
cd /sdcard/github/

read -p "Remove dotfiles Folder?" choice
case "$choice" in
  y|Y ) rm -rf dotfiles/;;
  n|N ) echo "Ok";;
  * ) echo "invalid";;
esac

read -p "Rerun dotfiles Updater?" choice
case "$choice" in
  y|Y ) sh /sdcard/github/dotfiles/Note-Termux.sh;;
  n|N ) exit;;
  * ) echo "invalid";;
esac
