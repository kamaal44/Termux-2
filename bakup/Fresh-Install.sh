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
pkg install -y captype
pkg install -y editcap
pkg install -y mergecap
pkg install -y rawshark
pkg install -y capinfos
pkg install -y randpkt
pkg install -y dumpcap
pkg install -y sharkd
pkg install -y idl2wrs
pkg install -y text2pcap
pkg install -y reordercap
pkg install -y lxc-top
pkg install -y lxc-unfreeze
pkg install -y lxc-update-config
pkg install -y lxc-unshare
pkg install -y lxc-setup-cgroups
pkg install -y openbox obconf
pkg install -y thunar
pkg install -y ranger
pkg install -y cmus
pkg install -y cava
pkg install -y lxc-console
pkg install -y lxc-monitor
pkg install -y lxc-create
pkg install -y lxc-execute
pkg install -y lxc-stop
pkg install -y lxc-usernsexec
pkg install -y lxc-destroy
pkg install -y lxc-cgroup
pkg install -y lxc-config
pkg install -y lxc-attach
pkg install -y lxc-copy
pkg install -y lxc-info
pkg install -y lxc-wait
pkg install -y lxc-freeze
pkg install -y lxc-start
pkg install -y lxc-device
pkg install -y jq
pkg install -y libxml2-utils
pkg install -y bc
pkg install -y httping
pkg install -y dnsutils openssh ffmpeg
pkg install -y lxc-checkpoint
pkg install -y lxc-ls
pkg install -y lxc-checkconfig
pkg install -y lxc-snapshot
pkg install -y lxc-autostart
pkg install -y init.lxc
pkg update -y
pkg upgrade -y
apt update -y
apt upgrade -y
pip install upgrade pip
npm install -g npm
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
mkdir -p /storage/emulated/0/github/
cd /storage/emulated/0/github/
git clone https://github.com/NateWeiler/Termux.git
cp -R /storage/emulated/0/github/Termux/home/.bashrc /data/data/com.termux/files/home/
cp -R /storage/emulated/0/github/Termux/home/.zshrc /data/data/com.termux/files/home/
cp -R /storage/emulated/0/github/Termux/home/.profile /data/data/com.termux/files/home/
cp -R /storage/emulated/0/github/Termux/home/aliases /data/data/com.termux/files/home/
cp -R /storage/emulated/0/github/Termux/home/functions /data/data/com.termux/files/home/
cp -R /storage/emulated/0/github/Termux/home/pad.txt /data/data/com.termux/files/home/
cp -R /storage/emulated/0/github/Termux/home/.gitconfig /data/data/com.termux/files/home/
cp -R /storage/emulated/0/github/Termux/home/etc /data/data/com.termux/files/home/
cp -R /storage/emulated/0/github/Termux/home/bin /data/data/com.termux/files/home/
clear
source /data/data/com.termux/files/home/aliases
cd /storage/emulated/0/github/Termux/installs/
echo "Updating Everything Again"
apt update -y
apt upgrade -y
pkg update -y
pkg upgrade -y
python3 -m pip install --upgrade pip
clear
sh /storage/emulated/0/github/Termux/installs/android.sh
sh /storage/emulated/0/github/Termux/installs/ansible.sh
sh /storage/emulated/0/github/Termux/installs/API.sh
sh /storage/emulated/0/github/Termux/installs/AutoPixie-WPS-Scan-Tool.sh
sh /storage/emulated/0/github/Termux/installs/busybox.sh
sh /storage/emulated/0/github/Termux/installs/caddy.sh
sh /storage/emulated/0/github/Termux/installs/CMSmap.sh
sh /storage/emulated/0/github/Termux/installs/Codiad.sh
sh /storage/emulated/0/github/Termux/installs/Compiling-and-setting-up-OCaml.sh
sh /storage/emulated/0/github/Termux/installs/Crontab.sh
sh /storage/emulated/0/github/Termux/installs/DarkFly-Tool.sh
sh /storage/emulated/0/github/Termux/installs/debian_on_termux_10.sh
sh /storage/emulated/0/github/Termux/installs/Debian-Install.sh
sh /storage/emulated/0/github/Termux/installs/debian-on-termux.sh
sh /storage/emulated/0/github/Termux/installs/desktop.sh
sh /storage/emulated/0/github/Termux/installs/Docker.sh
sh /storage/emulated/0/github/Termux/installs/Dorks-Eye.sh
sh /storage/emulated/0/github/Termux/installs/Dropbear.sh
sh /storage/emulated/0/github/Termux/installs/DVR.sh
sh /storage/emulated/0/github/Termux/installs/EasY-HaCk.sh
sh /storage/emulated/0/github/Termux/installs/emacs.sh
sh /storage/emulated/0/github/Termux/installs/Fish.sh
sh /storage/emulated/0/github/Termux/installs/FTP.sh
sh /storage/emulated/0/github/Termux/installs/FZF.sh
sh /storage/emulated/0/github/Termux/installs/Games.sh
sh /storage/emulated/0/github/Termux/installs/Graphical-Environment.sh
sh /storage/emulated/0/github/Termux/installs/gTTS.sh
sh /storage/emulated/0/github/Termux/installs/Heroku.sh
sh /storage/emulated/0/github/Termux/installs/Homebrew.sh
sh /storage/emulated/0/github/Termux/installs/HPomb.sh
sh /storage/emulated/0/github/Termux/installs/java.sh
sh /storage/emulated/0/github/Termux/installs/Kali.sh
sh /storage/emulated/0/github/Termux/installs/KickThemOut.sh
sh /storage/emulated/0/github/Termux/installs/MariaDB.sh
sh /storage/emulated/0/github/Termux/installs/Metasploit.sh
sh /storage/emulated/0/github/Termux/installs/MOSH.sh
sh /storage/emulated/0/github/Termux/installs/mpd.sh
sh /storage/emulated/0/github/Termux/installs/myserver.sh
sh /storage/emulated/0/github/Termux/installs/Neofetch.sh
sh /storage/emulated/0/github/Termux/installs/oh-my-termux.sh
sh /storage/emulated/0/github/Termux/installs/Oh-My-Zsh.sh
sh /storage/emulated/0/github/Termux/installs/OpenSSH.sh
sh /storage/emulated/0/github/Termux/installs/p10k-Font.sh
sh /storage/emulated/0/github/Termux/installs/Postgresql.sh
sh /storage/emulated/0/github/Termux/installs/PRoot.sh
sh /storage/emulated/0/github/Termux/installs/pyter.sh
sh /storage/emulated/0/github/Termux/installs/Python.sh
sh /storage/emulated/0/github/Termux/installs/pyttsx3.sh
sh /storage/emulated/0/github/Termux/installs/rbenv.sh
sh /storage/emulated/0/github/Termux/installs/rclone.sh
sh /storage/emulated/0/github/Termux/installs/Rsync.sh
sh /storage/emulated/0/github/Termux/installs/Ruby.sh
sh /storage/emulated/0/github/Termux/installs/RVM.sh
sh /storage/emulated/0/github/Termux/installs/services.sh
sh /storage/emulated/0/github/Termux/installs/Setting-up-HTTP-Server.sh
sh /storage/emulated/0/github/Termux/installs/Setting-up-Public-Key-Authentication.sh
sh /storage/emulated/0/github/Termux/installs/setup-pointless-repo.sh
sh /storage/emulated/0/github/Termux/installs/shells.sh
sh /storage/emulated/0/github/Termux/installs/Slack.sh
sh /storage/emulated/0/github/Termux/installs/Snoop.sh
sh /storage/emulated/0/github/Termux/installs/sms.sh
sh /storage/emulated/0/github/Termux/installs/SocialFish.sh
sh /storage/emulated/0/github/Termux/installs/Speak.sh
sh /storage/emulated/0/github/Termux/installs/Speak-Engine.sh
sh /storage/emulated/0/github/Termux/installs/sqlscan.sh
sh /storage/emulated/0/github/Termux/installs/ssh-apt.sh
sh /storage/emulated/0/github/Termux/installs/Sudo.sh
sh /storage/emulated/0/github/Termux/installs/Tool-X.sh
sh /storage/emulated/0/github/Termux/installs/TBomb.sh
sh /storage/emulated/0/github/Termux/installs/Terminal-Look-Awesome-Color-Font-Style.sh
sh /storage/emulated/0/github/Termux/installs/termux-fedora.sh
sh /storage/emulated/0/github/Termux/installs/termux-sms.sh
sh /storage/emulated/0/github/Termux/installs/tor.sh
sh /storage/emulated/0/github/Termux/installs/transmission.sh
sh /storage/emulated/0/github/Termux/installs/ubuntu.sh
sh /storage/emulated/0/github/Termux/installs/xfce4.sh
sh /storage/emulated/0/github/Termux/installs/youtube-dl.sh
sh /storage/emulated/0/github/Termux/installs/Zip.sh
unzip /storage/emulated/0/github/Termux/home/.ssh.zip /data/data/com.termux/files/home/.ssh
cd /storage/emulated/0/github/Termux/
mv -v .git DOTgit
find . -depth -type d -name ".git" -exec rm -rf {} \; && find . -depth -type d -name ".github" -exec rm -rf {} \;
mv -v DOTgit .git
cd /data/data/com.termux/files/home/
bash <(curl -fsSL https://git.io/JvMD6)
bash <(curl -fsSL https://git.io/JTgsU)
exit
