#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nTermux p10k Font Install"

cd /data/data/com.termux/files/home/

mkdir -p .termux

curl -fsSL -o /data/data/com.termux/files/home/.termux/font.ttf 'https://github.com/romkatv/dotfiles-public/raw/master/.local/share/fonts/NerdFonts/MesloLGS%20NF%20Regular.ttf'

termux-reload-settings
