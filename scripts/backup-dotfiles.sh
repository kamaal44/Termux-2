#!/bin/sh

cd /sdcard/github/
echo "Cloning dotfiles Repo"
git clone https://github.com/NateWeiler/dotfiles.git
cd dotfiles
echo "\Removing old Note-Termux Folder"
rm -rf Note-Termux/
mkdir -p Note-Termux
cd Note-Termux/
echo "\nZipping Note-Termux.zip"
zip -r -q Note-Termux.zip ~/Mail ~/Optiva-Framework ~/aliases ~/apktool ~/bin ~/buildAPKs ~/builtAPKs ~/codiad ~/crontab-testing ~/crontab.txt ~/data ~/debian-testing ~/deboot_debian ~/debootstrap ~/etc ~/export ~/files ~/functions ~/go ~/kali-fs ~/kali.sh ~/metasploit-framework ~/neofetch ~/oh-my-fish ~/pad.txt ~/prefix ~/progs ~/routersploit ~/start-kali.sh ~/start-ubuntu.sh ~/termux-desktop ~/termux.properties ~/tmp ~/ubuntu-fs ~/ubuntu.sh ~/xerxes
echo "\nUnzipping Note-Termux.zip\n"
unzip -qq Note-Termux.zip
mv -t /sdcard/github/dotfiles/Note-Termux/ data/data/com.termux/files/home/* data/data/com.termux/files/home/.*
echo "\nRemoving Note-Termux.zip\n"
rm -rf Note-Termux.zip data/data/
find . -depth -type d -name ".git" -exec rm -rf {} \;
find . -depth -type d -name ".github" -exec rm -rf {} \;
cd ..
echo "\nAdding files to Commit"
git add -Af
echo "\nCommitting files to Repo\n"
git commit -m "Note Termux"
echo "\nPushing files to Repo with Force\n"
git push -u --force origin master
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
