#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nHomebrew on Linux Installation"

pkg install -y git

pkg install -y ruby

pkg install -y curl

pkg install -y clang

pkg install -y proot

pkg install -y make

echo -e "\nGet a copy of linuxbrew:"

cd /data/data/com.termux/files/home/

git clone https://github.com/Linuxbrew/brew.git ~/prefix/brew

cd ~/prefix/brew

alias brew="termux-chroot $PWD/bin/brew"

echo -e '\nalias brew="termux-chroot $PWD/bin/brew"\n'

read -r -p "Are you sure? [Y/n]" response
response=${response,,} #   <-- tolower
if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then
   nano /data/data/com.termux/files/home/aliases
fi
