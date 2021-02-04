#!/data/data/com.termux/files/usr/bin/bash

echo "Termux Fresh Install"
echo "Grant Storage Permission"
termux-setup-storage
echo "Updating Everything"
apt update -y
apt upgrade -y
pkg update -y
pkg upgrade -y
clear
echo "Installing All Packages"
pkg install -y x11-repo
pkg install -y unstable-repo
pkg install -y root-repo
pkg install -y termux-api
pkg install -y debootstrap
pkg install -y nano
pkg install -y git
pkg install -y curl
pkg install -y dpkg
pkg install -y wget
pkg install -y imagemagick
pkg install -y zsh
pkg install -y gnupg
pkg install -y python
pkg install -y python2
pkg install -y vim
pkg install -y figlet
pkg install -y vim-python
pkg install -y openssh
pkg install -y mc
pkg install -y autoconf
pkg install -y uucp
pkg install -y automake
pkg install -y bison bzip2
pkg install -y clang
pkg install -y cmake
pkg install -y coreutils
pkg install -y diffutils
pkg install -y flex
pkg install -y gawk
pkg install -y grep
pkg install -y gzip
pkg install -y libtool
pkg install -y make
pkg install -y patch
pkg install -y perl
pkg install -y sed
pkg install -y silversearcher-ag
pkg install -y tar
pkg install -y apache2
pkg install -y php
pkg install -y php-apache
pkg install -y sox
pkg install -y pulseaudio
pkg install -y ffmpeg
pkg install -y tmux
pkg install -y build-essential
pkg install -y m4
pkg install -y libcurl
pkg install -y termux-tools
pkg install -y proot
pkg install -y util-linux
pkg install -y net-tools
pkg install -y tigervnc
pkg install -y openbox
pkg install -y obconf
pkg install -y xorg-xsetroot
pkg install -y xcompmgr
pkg install -y xterm
pkg install -y polybar
pkg install -y st
pkg install -y libnl
pkg install -y geany
pkg install -y pcmanfm
pkg install -y rofi
pkg install -y feh
pkg install -y neofetch
pkg install -y htop
pkg install -y elinks
pkg install -y mutt
pkg install -y xfce4-settings
pkg install -y fish
pkg install -y tsu
pkg install -y duf
pkg install -y gh
pkg install -y proj
pkg install -y wireless-tools
pkg install -y renameutils
pkg install -y git-gitk
pkg install -y termux-exec
pkg install -y termux-fix-shebang
pkg install -y game-repo
pkg install -y busybox
pkg install -y science-repo
pkg install -y pacman4console
pkg install -y ruby
pkg install -y ruby-ri
pkg install -y moreutils
pkg install -y task-spooler
pkg install -y yarn
pkg install -y hexcurse
pkg install -y hugo
pkg install -y ired
pkg install -y radare
pkg install -y icu-devtools
pkg install -y ldc
pkg install -y sleuthkit
pkg install -y nodejs
pkg install -y nodejs-lts
pkg install -y gettext
pkg install -y jupp
pkg install -y ocrad
pkg install -y tshark
pkg install -y libusbmuxd
pkg install -y nmh
pkg install -y cmatrix
pkg install -y mariadb
pkg install -y bastet
pkg install -y termux-services
pkg install -y moon-buggy
pkg install -y qemu-system
pkg install -y cronie
pkg install -y ninvaders
pkg install -y nsnake
pkg install -y greed
pkg install -y nethack
pkg install -y nudoku
pkg install -y libjpeg-turbo
pkg install -y libpng
pkg install -y python-tkinter
pkg install -y numpy
pkg install -y scipy
pkg install -y tcsh
pkg install -y beanshell
pkg install captype
pkg install editcap
pkg install mergecap
pkg install rawshark
pkg install capinfos
pkg install tshark
pkg install randpkt
pkg install dumpcap
pkg install sharkd
pkg install idl2wrs
pkg install text2pcap
pkg install reordercap
pkg install lxc-top
pkg install lxc-unfreeze
pkg install lxc-update-config
pkg install lxc-unshare
pkg install lxc-setup-cgroups
pkg install lxc-console
pkg install lxc-monitor
pkg install lxc-create
pkg install lxc-execute
pkg install lxc-stop
pkg install lxc-usernsexec
pkg install lxc-destroy
pkg install lxc-cgroup
pkg install lxc-config
pkg install lxc-attach
pkg install lxc-copy
pkg install lxc-info
pkg install lxc-wait
pkg install lxc-freeze
pkg install lxc-start
pkg install lxc-device
pkg install lxc-checkpoint
pkg install lxc-ls
pkg install lxc-checkconfig
pkg install lxc-snapshot
pkg install lxc-autostart
pkg install init.lxc
pkg update -y && pkg upgrade -y
apt update -y && apt upgrade -y
pip install upgrade pip; npm install -g npm
pkg install curl git wget python python2 nodejs jq libxml2-utils grep bc htop figlet httping dnsutils openssh ffmpeg
curl -sL https://gist.githubusercontent.com/mskian/6ea9c2b32d5f41867e7cafc88d1b26d5/raw/youtube-dl.sh | bash
pkg install php nano zsh
curl -sS https://getcomposer.org/installer | php -- --install-dir=/data/data/com.termux/files/usr/bin --filename=composer
pip install --upgrade pip setuptools
pip install --upgrade httpie
pip install -U requests[socks]
pip install requests
pkg install clang python-dev libffi-dev openssl-dev
pip install ddgr
pkg install screenfetch w3m termux-exec termux-api
pkg update -y && pkg upgrade -y
apt update -y && apt upgrade -y
pip install upgrade pip; npm install -g npm
termux-setup-storage
cd .termux
nano termux.properties
=extra-keys = [ \
 ['ESC','|','/','HOME','UP','END','PGUP','DEL'], \
 ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP'] \
]
termux-upgrade-repo
cd $HOME
ls
curl -sL https://gist.githubusercontent.com/mskian/4278fed4a206f4ec440f0dd512d4540b/raw/package.sh | bash
pkg list-installed > /storage/emulated/0/Download/pkgs.txt
hash -r

clear

echo "Installing All Applications"

apt install -y ruby
apt install -y zip
apt install -y unzip
apt install -y rsync
apt install -y nudoku
apt install -y texlive
apt install -y texlive-full
apt install -y nmap
apt install -y php
apt install -y python-dev
apt install -y libxml2-dev
apt install -y libxml2-utils
apt install -y libxslt-dev
apt install -y lynx
apt install -y figlet
apt install -y nano
apt install -y w3m
apt install -y clang
apt install -y hydra
apt install -y openssl
apt install -y libcurl
apt install -y wget
apt install -y perl
apt install -y ncurses-utils
apt install -y crunch
apt install -y gdb
apt install -y radare2
apt install -y ired
apt install -y ddrescue
apt install -y bin-utils
apt install -y yasm
apt install -y strace
apt install -y ltrace
apt install -y cdb
apt install -y hexcurse
apt install -y memcached
apt install -y llvmdb
apt install -y dpkg
apt install -y imagemagick
apt install -y unstable-repo
apt install -y hashcat
apt install -y libiconv
apt install -y zlib
apt install -y autoconf
apt install -y bison
apt install -y coreutils
apt install -y findutils
apt install -y apr
apt install -y apr-util
apt install -y libffi
apt install -y libgmp
apt install -y libpcap
apt install -y postgresql
apt install -y readline
apt install -y libsqlite
apt install -y libtool
apt install -y libxml2
apt install -y libxslt
apt install -y ncurses
apt install -y pkg-config
apt install -y make
apt install -y libgrpc
apt install -y termux-tools
apt install -y tar
apt install -y termux-elf-cleaner
apt install -y zsh
apt-get update -y
apt-get install -y xfce4
apt-get install -y xfce4-terminal
apt-get install -y tightvncserver
apt-get install -y xfe
apt update > /dev/null 2>&1
apt --assumees install wget > /dev/null 2>&1
apt autoremove
apt-get clean
clear
mkdir -p /data/data/com.termux/files/home/backups/
mkdir -p /sdcard/github/
cd /sdcard/github/
git clone https://github.com/NateWeiler/Termux.git
cp -R /sdcard/github/Termux/home/.bashrc /data/data/com.termux/files/home/
cp -R /sdcard/github/Termux/home/.zshrc /data/data/com.termux/files/home/
cp -R /sdcard/github/Termux/home/.profile /data/data/com.termux/files/home/
cp -R /sdcard/github/Termux/home/aliases /data/data/com.termux/files/home/
cp -R /sdcard/github/Termux/home/functions /data/data/com.termux/files/home/
cp -R /sdcard/github/Termux/home/pad.txt /data/data/com.termux/files/home/
cp -R /sdcard/github/Termux/home/.gitconfig /data/data/com.termux/files/home/
cp -R /sdcard/github/Termux/home/etc /data/data/com.termux/files/home/
cp -R /sdcard/github/Termux/home/bin /data/data/com.termux/files/home/
clear
source /data/data/com.termux/files/home/aliases
cd /sdcard/github/Termux/installs/
echo "Updating Everything Again"
apt update -y
apt upgrade -y
pkg update -y
pkg upgrade -y
python3 -m pip install --upgrade pip
clear
sh /sdcard/github/Termux/installs/android.sh
sh /sdcard/github/Termux/installs/ansible.sh
sh /sdcard/github/Termux/installs/API.sh
sh /sdcard/github/Termux/installs/AutoPixie-WPS-Scan-Tool.sh
sh /sdcard/github/Termux/installs/busybox.sh
sh /sdcard/github/Termux/installs/caddy.sh
sh /sdcard/github/Termux/installs/CMSmap.sh
sh /sdcard/github/Termux/installs/Codiad.sh
sh /sdcard/github/Termux/installs/Compiling-and-setting-up-OCaml.sh
sh /sdcard/github/Termux/installs/Crontab.sh
sh /sdcard/github/Termux/installs/DarkFly-Tool.sh
sh /sdcard/github/Termux/installs/debian_on_termux_10.sh
sh /sdcard/github/Termux/installs/Debian-Install.sh
sh /sdcard/github/Termux/installs/debian-on-termux.sh
sh /sdcard/github/Termux/installs/desktop.sh
sh /sdcard/github/Termux/installs/Docker.sh
sh /sdcard/github/Termux/installs/Dorks-Eye.sh
sh /sdcard/github/Termux/installs/Dropbear.sh
sh /sdcard/github/Termux/installs/DVR.sh
sh /sdcard/github/Termux/installs/EasY-HaCk.sh
sh /sdcard/github/Termux/installs/emacs.sh
sh /sdcard/github/Termux/installs/Fish.sh
sh /sdcard/github/Termux/installs/FTP.sh
sh /sdcard/github/Termux/installs/FZF.sh
sh /sdcard/github/Termux/installs/Games.sh
sh /sdcard/github/Termux/installs/Graphical-Environment.sh
sh /sdcard/github/Termux/installs/gTTS.sh
sh /sdcard/github/Termux/installs/Heroku.sh
sh /sdcard/github/Termux/installs/Homebrew.sh
sh /sdcard/github/Termux/installs/HPomb.sh
sh /sdcard/github/Termux/installs/java.sh
sh /sdcard/github/Termux/installs/Kali.sh
sh /sdcard/github/Termux/installs/KickThemOut.sh
sh /sdcard/github/Termux/installs/MariaDB.sh
sh /sdcard/github/Termux/installs/Metasploit.sh
sh /sdcard/github/Termux/installs/MOSH.sh
sh /sdcard/github/Termux/installs/mpd.sh
sh /sdcard/github/Termux/installs/myserver.sh
sh /sdcard/github/Termux/installs/Neofetch.sh
sh /sdcard/github/Termux/installs/oh-my-termux.sh
sh /sdcard/github/Termux/installs/Oh-My-Zsh.sh
sh /sdcard/github/Termux/installs/OpenSSH.sh
sh /sdcard/github/Termux/installs/p10k-Font.sh
sh /sdcard/github/Termux/installs/Postgresql.sh
sh /sdcard/github/Termux/installs/PRoot.sh
sh /sdcard/github/Termux/installs/pyter.sh
sh /sdcard/github/Termux/installs/Python.sh
sh /sdcard/github/Termux/installs/pyttsx3.sh
sh /sdcard/github/Termux/installs/rbenv.sh
sh /sdcard/github/Termux/installs/rclone.sh
sh /sdcard/github/Termux/installs/Rsync.sh
sh /sdcard/github/Termux/installs/Ruby.sh
sh /sdcard/github/Termux/installs/RVM.sh
sh /sdcard/github/Termux/installs/services.sh
sh /sdcard/github/Termux/installs/Setting-up-HTTP-Server.sh
sh /sdcard/github/Termux/installs/Setting-up-Public-Key-Authentication.sh
sh /sdcard/github/Termux/installs/setup-pointless-repo.sh
sh /sdcard/github/Termux/installs/shells.sh
sh /sdcard/github/Termux/installs/Slack.sh
sh /sdcard/github/Termux/installs/Snoop.sh
sh /sdcard/github/Termux/installs/sms.sh
sh /sdcard/github/Termux/installs/SocialFish.sh
sh /sdcard/github/Termux/installs/Speak.sh
sh /sdcard/github/Termux/installs/Speak-Engine.sh
sh /sdcard/github/Termux/installs/sqlscan.sh
sh /sdcard/github/Termux/installs/ssh-apt.sh
sh /sdcard/github/Termux/installs/Sudo.sh
sh /sdcard/github/Termux/installs/Tool-X.sh
sh /sdcard/github/Termux/installs/TBomb.sh
sh /sdcard/github/Termux/installs/Terminal-Look-Awesome-Color-Font-Style.sh
sh /sdcard/github/Termux/installs/termux-fedora.sh
sh /sdcard/github/Termux/installs/termux-sms.sh
sh /sdcard/github/Termux/installs/tor.sh
sh /sdcard/github/Termux/installs/transmission.sh
sh /sdcard/github/Termux/installs/ubuntu.sh
sh /sdcard/github/Termux/installs/xfce4.sh
sh /sdcard/github/Termux/installs/youtube-dl.sh
sh /sdcard/github/Termux/installs/Zip.sh
unzip /sdcard/github/Termux/home/.ssh.zip /data/data/com.termux/files/home/.ssh
cd /sdcard/github/Termux/
mv -v .git DOTgit
find . -depth -type d -name ".git" -exec rm -rf {} \; && find . -depth -type d -name ".github" -exec rm -rf {} \;
mv -v DOTgit .git
cd /data/data/com.termux/files/home/
bash <(curl -fsSL https://git.io/JvMD6)
bash <(curl -fsSL https://git.io/JTgsU)
exit
