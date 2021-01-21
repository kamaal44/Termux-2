#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nMake Termux terminal look Awesome Install"

echo -e "\nColor, Font, Style"

apt update -y

apt upgrade -y

apt install -y curl

clear

cd /sdcard/github/Termux/installs/

sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"

echo -e "\nwait for complete install and choose any option according to you."

echo -e "\nfor Example:"

echo -e "\ntype 0"

echo -e "\nand restart termux app"

echo -e "\nIf you need Change color scheme then type"

echo -e "\n~/.termux/colors.sh"

echo -e "\nIf you need Change font then type"

echo -e "\n~/.termux/fonts.sh"
