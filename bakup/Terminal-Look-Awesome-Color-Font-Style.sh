#!/data/data/com.termux/files/usr/bin/sh

echo "\nMake Termux terminal look Awesome Install"

echo "\nColor, Font, Style"

apt update -y

apt upgrade -y

apt install -y curl

clear

cd /sdcard/github/Termux/installs/

sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"

echo "\nwait for complete install and choose any option according to you."

echo "\nfor Example:"

echo "\ntype 0"

echo "\nand restart termux app"

echo "\nIf you need Change color scheme then type"

echo "\n~/.termux/colors.sh"

echo "\nIf you need Change font then type"

echo "\n~/.termux/fonts.sh"
