#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nUbuntu Install"

cd /data/data/com.termux/files/home/

USER=$(whoami)

export DEBIAN_FRONTEND=noninteractive

export PATH="#!/data/data/com.termux/files/home/.local/bin:$PATH"

rm -rf /var/lib/dpkg/lock

rm -rf /var/cache/debconf/*.*

# colors
NORMAL=`tput sgr0`
RED=`tput setaf 1`
GREEN=`tput setaf 2`
Done="${GREEN}Done ✓${NORMAL}"

clear

echo -e "\n${RED}Disclaimer:${NORMAL} This script is shit and bloated"

sleep 5

echo -e "\n${RED}Do you want to change server password?${NORMAL}"
read -p "y/n:
" prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]
then
  passwd $USER
else
  echo -e "\n${GREEN}Password wasn't Changed.${NORMAL}"
fi

echo -e "\n${RED}Enabling Universe, Multiverse and Restricted repositories${NORMAL}"

sleep 1

add-apt-repository universe > /dev/null

add-apt-repository multiverse > /dev/null

add-apt-repository restricted > /dev/null

echo $Done

echo -e "\n${RED}Checking for updates.${NORMAL}"

sleep 1

apt-get -y update > /dev/null

apt-get -y upgrade > /dev/null 2>&1

apt-get -y autoremove  > /dev/null

echo $Done

echo -e "\n${RED}Setting UTF8${NORMAL}"

sleep 1

export LC_ALL=en_US.UTF-8

export LANG=en_US.UTF-8

apt-get install -qq language-pack-en-base > /dev/null

apt-get install -qq software-properties-common > /dev/null

echo $Done

echo -e "\n${RED}Adding a auto updater to crontab${NORMAL}"

sleep 1

crontab -l > updater

echo -e "\n0 0 * * *    apt-get update

apt-get upgrade -y

apt autoremove

echo updated@SUCCESS >> /data/data/com.termux/files/home/.update.log" >> updater

crontab updater

rm -rf updater

echo $Done

echo -e "\n${RED}Installing Apt-fast${NORMAL}"

add-apt-repository -y ppa:apt-fast/stable > /dev/null

apt-get -qq update > /dev/null

DEBIAN_FRONTEND=noninteractive apt-get -y install apt-fast > /dev/null 

echo $Done

echo -e "\n${RED}Installing day2day packages${NORMAL}"

apt-get install -qq ncdu tmux irssi tree rar unrar zip unzip htop atop p7zip-full neovim vnstati > /dev/null 2>&1

echo $Done

echo -e "\n${RED}Now installing some python essential packages${NORMAL}"

apt-get install -qq python3-pip python3-dev python3-utmp python3-virtualenv > /dev/null 2>&1

echo $Done

echo -e "\n${RED}Installing rclone${NORMAL}"

sleep 1

curl -s https://rclone.org/install.sh | bash > /dev/null 2>&1

echo $Done

echo -e "\n${RED}Installing vsftpd${NORMAL}"

apt-get install -qq vsftpd  > /dev/null

systemctl start vsftpd  > /dev/null 2>&1

systemctl enable vsftpd > /dev/null 2>&1

tee -a /etc/vsftpduserlist.conf >> /dev/null <<'user'
ubuntu
towha
root
user

systemctl restart vsftpd  > /dev/null 2>&1

echo $Done

echo -e "\n${RED}Installing some compiling packages${NORMAL}"

apt-get install -qq build-essential libssl-dev autoconf automake cmake ccache libicu-dev git-core libass-dev zlib1g-dev yasm texinfo pkg-config libtool > /dev/null 2>&1

echo $Done

echo -e "\n${RED}Installing ffmpeg, please refer to https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu for extra codecs${NORMAL}"

sleep 5

apt-get install -qq ffmpeg > /dev/null 2>&1

echo $Done

echo -e "\n${RED}Installing Language packages${NORMAL}"

add-apt-repository -y ppa:openjdk-r/ppa > /dev/null

add-apt-repository -y ppa:linuxuprising/libpng12 > /dev/null # I am skipping php due to reasons and only adding its repo in case there is a need to install it.

apt-get install -qq nginx golang docker.io perl openjdk-15-jre > /dev/null 2>&1

curl -sL https://deb.nodesource.com/setup_14.x | -E bash - > /dev/null

apt-get -y install nodejs > /dev/null

echo $Done # apt-get install -qq curl debconf-utils php-pear php7.4-curl php7.4-dev php7.4-gd php7.4-mbstring php7.4-zip php7.4-mysql php7.4-xml php7.4-fpm php7.4-intl php7.4-bcmath > /dev/null 

echo -e "\n${RED}Installing aria2 & transmission${NORMAL}"

apt-get install -qq aria2 > /dev/null

apt-get install -qq transmission-cli transmission-daemon > /dev/null

/etc/init.d/transmission-daemon stop > /dev/null

mkdir -p /data/data/com.termux/files/home/downloads

chown ubuntu:debian-transmission /data/data/com.termux/files/home/downloads

chmod g+w /data/data/com.termux/files/home/downloads

clear

sed -i 's|"/var/lib/transmission-daemon/downloads"|"/data/data/com.termux/files/home/downloads"|g' /etc/transmission-daemon/settings.json

sed -i 's|"rpc-whitelist-enabled": true|"rpc-whitelist-enabled": false|g' /etc/transmission-daemon/settings.json

sed -i 's|"rpc-authentication-required": true|"rpc-authentication-required": false|g' /etc/transmission-daemon/settings.json > /dev/null

echo $Done

echo -e "\n${RED}changing MOTD${NORMAL}" # "touch .hushlogin" to "remove" the motd instead of deleting it.

apt-get install -qq update-motd > /dev/null

rm -rf /etc/update-motd.d/*

apt-get install -qq inxi screenfetch > /dev/null

touch /etc/update-motd.d/01-custom

chmod +x /etc/update-motd.d/01-custom

tee /etc/update-motd.d/01-custom > /dev/null <<'MOTD'
#!/bin/bash
echo GENERAL SYSTEM INFORMATION
/usr/bin/screenfetch
echo
echo SYSTEM DISK USAGE
export TERM=xterm; inxi -D
echo
MOTD
echo $Done

echo -e "\n${RED}Now installing oh-my-tmux${NORMAL}"
cd

git clone --quiet https://github.com/gpakosz/.tmux.git > /dev/null

ln -s -f .tmux/.tmux.conf > /dev/null

cp .tmux/.tmux.conf.local .

echo $Done

echo -e "\n${RED}Now installing ZSH${NORMAL}"

sleep 1

apt-get update -qq

apt-get install -qq zsh > /dev/null 2>&1

\
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

echo -e "${GREEN}Making Oh My Zsh hawt...${NORMAL}"

git clone --quiet https://github.com/zsh-users/zsh-syntax-highlighting /data/data/com.termux/files/home/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting > /dev/null 

git clone --quiet https://github.com/zsh-users/zsh-autosuggestions /data/data/com.termux/files/home/.oh-my-zsh/custom/plugins/zsh-autosuggestions > /dev/null 

git clone --quiet https://github.com/zsh-users/zsh-completions /data/data/com.termux/files/home/.oh-my-zsh/custom/plugins/zsh-completions > /dev/null 

wget https://raw.githubusercontent.com/rupa/z/master/z.sh -q -O /data/data/com.termux/files/home/.z > /dev/null 2>&1

git clone --quiet --depth=1 https://github.com/romkatv/powerlevel10k.git /data/data/com.termux/files/home/.oh-my-zsh/custom/themes/powerlevel10k > /dev/null
[[ -z $(grep "autoload -U compinit

compinit" /data/data/com.termux/files/home/.zshrc) ]]

echo -e "\nautoload -U compinit

compinit" >> /data/data/com.termux/files/home/.zshrc

sed -i '/^ZSH_THEME=/c\ZSH_THEME="random"' /data/data/com.termux/files/home/.zshrc

sed -i '/^plugins=*=/c\plugins=(command-not-found tmux tmuxinator jump z zsh-syntax-highlighting zsh-autosuggestions zsh-completions)' /data/data/com.termux/files/home/.zshrc

echo -e "\nexport PATH=\"/home/$USER/.local/bin:\$PATH\"" >> /data/data/com.termux/files/home/.zshrc 

tee -a /data/data/com.termux/files/home/.zshrc >> /dev/null <<'ALIAS'

#chsh -s /bin/zsh $USER

echo -e "\nbash -c zsh" >> .bashrc # This is used since for some cloud service changing the shell isn't permitted so a work around for it.

echo $Done

echo -e "\n${GREEN}ALL DONE!${NORMAL}"

echo -e "\n${GREEN}It is recommended to ${RED}reboot${NORMAL}${GREEN} your server now!${NORMAL}"
