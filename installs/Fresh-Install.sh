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
sh /data/data/com.termux/files/installs/android.sh
sh /data/data/com.termux/files/installs/ansible.sh
sh /data/data/com.termux/files/installs/API.sh
sh /data/data/com.termux/files/installs/AutoPixie-WPS-Scan-Tool.sh
sh /data/data/com.termux/files/installs/busybox.sh
sh /data/data/com.termux/files/installs/caddy.sh
sh /data/data/com.termux/files/installs/CMSmap.sh
sh /data/data/com.termux/files/installs/Codiad.sh
sh /data/data/com.termux/files/installs/Compiling-and-setting-up-OCaml.sh
sh /data/data/com.termux/files/installs/Crontab.sh
sh /data/data/com.termux/files/installs/DarkFly-Tool.sh
sh /data/data/com.termux/files/installs/debian_on_termux_10.sh
sh /data/data/com.termux/files/installs/Debian-Install.sh
sh /data/data/com.termux/files/installs/debian-on-termux.sh
sh /data/data/com.termux/files/installs/desktop.sh
sh /data/data/com.termux/files/installs/Docker.sh
sh /data/data/com.termux/files/installs/Dorks-Eye.sh
sh /data/data/com.termux/files/installs/Dropbear.sh
sh /data/data/com.termux/files/installs/DVR.sh
sh /data/data/com.termux/files/installs/EasY-HaCk.sh
sh /data/data/com.termux/files/installs/emacs.sh
sh /data/data/com.termux/files/installs/Fish.sh
sh /data/data/com.termux/files/installs/FTP.sh
sh /data/data/com.termux/files/installs/FZF.sh
sh /data/data/com.termux/files/installs/Games.sh
sh /data/data/com.termux/files/installs/Graphical-Environment.sh
sh /data/data/com.termux/files/installs/gTTS.sh
sh /data/data/com.termux/files/installs/Heroku.sh
sh /data/data/com.termux/files/installs/Homebrew.sh
sh /data/data/com.termux/files/installs/HPomb.sh
sh /data/data/com.termux/files/installs/java.sh
sh /data/data/com.termux/files/installs/Kali.sh
sh /data/data/com.termux/files/installs/KickThemOut.sh
sh /data/data/com.termux/files/installs/MariaDB.sh
sh /data/data/com.termux/files/installs/Metasploit.sh
sh /data/data/com.termux/files/installs/MOSH.sh
sh /data/data/com.termux/files/installs/mpd.sh
sh /data/data/com.termux/files/installs/myserver.sh
sh /data/data/com.termux/files/installs/Neofetch.sh
sh /data/data/com.termux/files/installs/oh-my-termux.sh
sh /data/data/com.termux/files/installs/Oh-My-Zsh.sh
sh /data/data/com.termux/files/installs/OpenSSH.sh
sh /data/data/com.termux/files/installs/p10k-Font.sh
sh /data/data/com.termux/files/installs/Postgresql.sh
sh /data/data/com.termux/files/installs/PRoot.sh
sh /data/data/com.termux/files/installs/pyter.sh
sh /data/data/com.termux/files/installs/Python.sh
sh /data/data/com.termux/files/installs/pyttsx3.sh
sh /data/data/com.termux/files/installs/rbenv.sh
sh /data/data/com.termux/files/installs/rclone.sh
sh /data/data/com.termux/files/installs/Rsync.sh
sh /data/data/com.termux/files/installs/Ruby.sh
sh /data/data/com.termux/files/installs/RVM.sh
sh /data/data/com.termux/files/installs/services.sh
sh /data/data/com.termux/files/installs/Setting-up-HTTP-Server.sh
sh /data/data/com.termux/files/installs/Setting-up-Public-Key-Authentication.sh
sh /data/data/com.termux/files/installs/setup-pointless-repo.sh
sh /data/data/com.termux/files/installs/shells.sh
sh /data/data/com.termux/files/installs/Slack.sh
sh /data/data/com.termux/files/installs/Snoop.sh
sh /data/data/com.termux/files/installs/sms.sh
sh /data/data/com.termux/files/installs/SocialFish.sh
sh /data/data/com.termux/files/installs/Speak.sh
sh /data/data/com.termux/files/installs/Speak-Engine.sh
sh /data/data/com.termux/files/installs/sqlscan.sh
sh /data/data/com.termux/files/installs/ssh-apt.sh
sh /data/data/com.termux/files/installs/Sudo.sh
sh /data/data/com.termux/files/installs/Tool-X.sh
sh /data/data/com.termux/files/installs/TBomb.sh
sh /data/data/com.termux/files/installs/Terminal-Look-Awesome-Color-Font-Style.sh
sh /data/data/com.termux/files/installs/termux-fedora.sh
sh /data/data/com.termux/files/installs/termux-sms.sh
sh /data/data/com.termux/files/installs/tor.sh
sh /data/data/com.termux/files/installs/transmission.sh
sh /data/data/com.termux/files/installs/ubuntu.sh
sh /data/data/com.termux/files/installs/xfce4.sh
sh /data/data/com.termux/files/installs/youtube-dl.sh
sh /data/data/com.termux/files/installs/Zip.sh
unzip /sdcard/github/Termux/home/.ssh.zip /data/data/com.termux/files/home/.ssh
cd /sdcard/github/Termux/
mv -v .git DOTgit
find . -depth -type d -name ".git" -exec rm -rf {} \; && find . -depth -type d -name ".github" -exec rm -rf {} \;
cd /data/data/com.termux/files/home/
mv -v DOTgit .git
bash <(curl -fsSL https://git.io/JvMD6)
bash <(curl -fsSL https://git.io/JTgsU)
exit
