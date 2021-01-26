#!/data/data/com.termux/files/usr/bin/bash

echo "Termux Fresh Install"
echo "\nGrant Storage Permission"
termux-setup-storage
echo "\nUpdating Everything"
apt update -y
apt upgrade -y
pkg update -y
pkg upgrade -y
clear
echo "\nInstalling All Packages"
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
pkg install -y openssh
pkg install -y tigervnc
pkg install -y openbox
pkg install -y obconf
pkg install -y xorg-xsetroot
pkg install -y xcompmgr
pkg install -y xterm
pkg install -y polybar
pkg install -y termux-api
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
pkg install -y coreutils
pkg install -y termux-tools
pkg install -y proot
pkg install -y util-linux
pkg install -y net-tools
pkg install -y openssh
pkg install -y git
pkg install -y wget
pkg install -y ocrad
pkg install -y tshark
pkg install -y libusbmuxd
pkg install -y nmh
pkg install -y cmatrix
pkg install -y tigervnc
pkg install -y x11-repo
pkg install -y mariadb
pkg install -y bastet
pkg install -y pacman4console
pkg install -y termux-services
pkg install -y moon-buggy
pkg install -y php
pkg install -y qemu-system
pkg install -y cronie
pkg install -y termux-services
pkg install -y ninvaders
pkg install -y nsnake
pkg install -y greed
pkg install -y build-essential
pkg install -y diffutils
pkg install -y m4
pkg install -y patch
pkg install -y nethack
pkg install -y nudoku
pkg install -y build-essential
pkg install -y cmake
pkg install -y libjpeg-turbo
pkg install -y libpng
pkg install -y python-tkinter
pkg install -y curl
pkg install -y python
pkg install -y ffmpeg
pkg install -y numpy
pkg install -y scipy
pkg install -y tcsh
pkg install -y beanshell
pkg install -y fish
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
clear
echo "\nInstalling All Applications"
apt install -y ruby
apt install -y zip
apt install -y unzip
apt install -y rsync
apt install -y nudoku
apt install -y texlive
apt install -y texlive-full
apt install -y nudoku
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
echo "\nUpdating Everything Again"
apt update -y
apt upgrade -y
pkg update -y
pkg upgrade -y
python3 -m pip install --upgrade pip
clear
sh android.sh
sh ansible.sh
sh API.sh
sh AutoPixie-WPS-Scan-Tool.sh
sh busybox.sh
sh caddy.sh
sh CMSmap.sh
sh Codiad.sh
sh Compiling-and-setting-up-OCaml.sh
sh Crontab.sh
sh DarkFly-Tool.sh
sh debian_on_termux_10.sh
sh Debian-Install.sh
sh debian-on-termux.sh
sh desktop.sh
sh Docker.sh
sh Dorks-Eye.sh
sh Dropbear.sh
sh DVR.sh
sh EasY-HaCk.sh
sh emacs.sh
sh Fish.sh
sh FTP.sh
sh FZF.sh
sh Games.sh
sh Graphical-Environment.sh
sh gTTS.sh
sh Heroku.sh
sh Homebrew.sh
sh HPomb.sh
sh java.sh
sh Kali.sh
sh KickThemOut.sh
sh MariaDB.sh
sh Metasploit.sh
sh MOSH.sh
sh mpd.sh
sh myserver.sh
sh Neofetch.sh
sh oh-my-termux.sh
sh Oh-My-Zsh.sh
sh OpenSSH.sh
sh p10k-Font.sh
sh Postgresql.sh
sh PRoot.sh
sh pyter.sh
sh Python.sh
sh pyttsx3.sh
sh rbenv.sh
sh rclone.sh
sh Rsync.sh
sh Ruby.sh
sh RVM.sh
sh services.sh
sh Setting-up-HTTP-Server.sh
sh Setting-up-Public-Key-Authentication.sh
sh setup-pointless-repo.sh
sh shells.sh
sh Slack.sh
sh Snoop.sh
sh sms.sh
sh SocialFish.sh
sh Speak.sh
sh Speak-Engine.sh
sh sqlscan.sh
sh ssh-apt.sh
sh Sudo.sh
sh Tool-X.sh
sh TBomb.sh
sh Terminal-Look-Awesome-Color-Font-Style.sh
sh termux-fedora.sh
sh termux-sms.sh
sh tor.sh
sh transmission.sh
sh ubuntu.sh
sh xfce4.sh
sh youtube-dl.sh
sh Zip.sh
unzip /sdcard/github/Termux/home/.ssh.zip /data/data/com.termux/files/home/.ssh
cd /sdcard/github/Termux/
mv -v .git DOTgit
find . -depth -type d -name ".git" -exec rm -rf {} \; && find . -depth -type d -name ".github" -exec rm -rf {} \;
cd /data/data/com.termux/files/home/
mv -v DOTgit .git
bash <(curl -fsSL https://git.io/JvMD6)
bash <(curl -fsSL https://git.io/JTgsU)
exit
