#!/data/data/com.termux/files/usr/bin/bash

echo "Termux Fresh Install"

echo "Grant Storage Permission"
termux-setup-storage
echo "Updating Everything"
termux-upgrade-repo
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
pkg install -y blackbox
pkg install -y dcraw
pkg install -y gh
pkg install -y git
pkg install -y git-crypt
pkg install -y git-delta
pkg install -y git-gitk
pkg install -y git-gui
pkg install -y git-lfs
pkg install -y gitea
pkg install -y gitflow-avh
pkg install -y gogs
pkg install -y hub
pkg install -y lazygit
pkg install -y libgit2
pkg install -y qgit
pkg install -y sleuthkit
pkg install -y texlive-langitalian
pkg install -y tig
pkg install -y vcsh
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
pkg install -y coreutils
pkg install -y dropbear
pkg install -y graphviz
pkg install -y nmap
pkg install -y nmh
pkg install -y openssh
pkg install -y procps
pkg install -y psutils
pkg install -y secure-delete
pkg install -y sharutils
pkg install -y snake
pkg install -y stag
pkg install -y tin-summer
pkg install -y gap
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
pkg install -y php
pkg install -y zsh
pkg install -y clang
pkg install -y python-dev
pkg install -y libffi-dev
pkg install -y openssl-dev
pkg install -y mlocate && updatedb
pkg install -y aalib
pkg install -y aapt
pkg install -y abduco
pkg install -y abook
pkg install -y ack-grep
pkg install -y adwaita-icon-theme
pkg install -y age
pkg install -y aircrack-ng
pkg install -y aircrack-ng-static algernon
pkg install -y angband
pkg install -y antibody
pkg install -y apksigner
pkg install -y apt
pkg install -y apt-ftparchive
pkg install -y apt-transport-tor
pkg install -y aptly
pkg install -y argp
pkg install -y aria2
pkg install -y arp-scan
pkg install -y asciidoc
pkg install -y asciinema
pkg install -y aspell
pkg install -y aspell-en
pkg install -y at
pkg install -y atomicparsley
pkg install -y atomvm
pkg install -y attr
pkg install -y autoconf
pkg install -y autoconf213
pkg install -y automake
pkg install -y axel
pkg install -y azpainter
pkg install -y barcode
pkg install -y bash-completion
pkg install -y bastet
pkg install -y bat
pkg install -y bc
pkg install -y beanshell
pkg install -y bftpd
pkg install -y bgrep
pkg install -y binutils
pkg install -y binutils-gold
pkg install -y bison
pkg install -y blackbox
pkg install -y blogc
pkg install -y bochs
pkg install -y boinc
pkg install -y boinctui
pkg install -y borgbackup
pkg install -y brogue
pkg install -y brook
pkg install -y brotli
pkg install -y bsdtar
pkg install -y build-essential
pkg install -y busybox
pkg install -y byobu
pkg install -y bzip2
pkg install -y c-ares
pkg install -y cabextract
pkg install -y caddy
pkg install -y calcurse
pkg install -y capnproto
pkg install -y capstone
pkg install -y cavez-of-phear
pkg install -y cboard
pkg install -y ccls
pkg install -y ccnet
pkg install -y cfengine
pkg install -y screenfetch
pkg install -y w3m
pkg install -y termux-exec
pkg install -y termux-api
pkg update -y
pkg upgrade -y
pkg autoclean
pip install upgrade pip; npm install -g npm
termux-setup-storage
cd $HOME/.termux
echo "\n=extra-keys = [ \
echo " ['ESC','|','/','HOME','UP','END','PGUP','DEL'], \"
echo " ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP'] \"
echo "]\n"
echo -e "\n${RED}"Are you sure?${NORMAL}"
read -p "y/n:
" prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt ==
"yes" || $prompt == "Yes" ]]
then
  nano termux.properties
else
  echo -e "\ntouch termux.properties"
fi
cle$HOMEions"
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
apt update -y
apt upgrade -y
apt autoremove
apt-get clean
clear
cd /data/data/com.termux/files/home
ls
curl -sL https://gist.githubusercontent.com/mskian/4278fed4a206f4ec440f0dd512d4540b/raw/package.sh | bash
pkg list-installed > /storage/emulated/0/Download/pkgs.txt
hash -r
clear
pip install --upgrade pip
pip install setuptools
pip install httpie
pip install -U requests[socks]
pip install requests
pip install ddgr
clear
npm install -g npm
curl -sL https://gist.githubusercontent.com/mskian/6ea9c2b32d5f41867e7cafc88d1b26d5/raw/youtube-dl.sh | bash
curl -sS https://getcomposer.org/installer | php -- --install-dir=/data/data/com.termux/files/usr/bin --filename=composer
mkdir -p $HOME/backups/
mkdir -p /storage/emulated/0/github/
cd /storage/emulated/0/github/
clear
git clone https://github.com/NateWeiler/Termux.git
mv -t -f /storage/emulated/0/github/Termux/home/ $HOME/ $HOME/
clear
source $HOME/aliases
cd /storage/emulated/0/github/Termux/installs/
echo "Updating Everything Again"
apt update -y
apt upgrade -y
pkg update -y
pkg upgrade -y
python3 -m pip install --upgrade pip
clear;sh /storage/emulated/0/github/Termux/installs/android.sh
clear;sh /storage/emulated/0/github/Termux/installs/ansible.sh
clear;sh /storage/emulated/0/github/Termux/installs/API.sh
clear;sh /storage/emulated/0/github/Termux/installs/AutoPixie-WPS-Scan-Tool.sh
clear;sh /storage/emulated/0/github/Termux/installs/busybox.sh
clear;sh /storage/emulated/0/github/Termux/installs/caddy.sh
clear;sh /storage/emulated/0/github/Termux/installs/CMSmap.sh
clear;sh /storage/emulated/0/github/Termux/installs/Codiad.sh
clear;sh /storage/emulated/0/github/Termux/installs/Compiling-and-setting-up-OCaml.sh
clear;sh /storage/emulated/0/github/Termux/installs/Crontab.sh
clear;sh /storage/emulated/0/github/Termux/installs/DarkFly-Tool.sh
clear;sh /storage/emulated/0/github/Termux/installs/debian_on_termux_10.sh
clear;sh /storage/emulated/0/github/Termux/installs/Debian-Install.sh
clear;sh /storage/emulated/0/github/Termux/installs/debian-on-termux.sh
clear;sh /storage/emulated/0/github/Termux/installs/desktop.sh
clear;sh /storage/emulated/0/github/Termux/installs/Docker.sh
clear;sh /storage/emulated/0/github/Termux/installs/Dorks-Eye.sh
clear;sh /storage/emulated/0/github/Termux/installs/Dropbear.sh
clear;sh /storage/emulated/0/github/Termux/installs/DVR.sh
clear;sh /storage/emulated/0/github/Termux/installs/EasY-HaCk.sh
clear;sh /storage/emulated/0/github/Termux/installs/emacs.sh
clear;sh /storage/emulated/0/github/Termux/installs/Fish.sh
clear;sh /storage/emulated/0/github/Termux/installs/FTP.sh
clear;sh /storage/emulated/0/github/Termux/installs/FZF.sh
clear;sh /storage/emulated/0/github/Termux/installs/Games.sh
clear;sh /storage/emulated/0/github/Termux/installs/Graphical-Environment.sh
clear;sh /storage/emulated/0/github/Termux/installs/gTTS.sh
clear;sh /storage/emulated/0/github/Termux/installs/Heroku.sh
clear;sh /storage/emulated/0/github/Termux/installs/Homebrew.sh
clear;sh /storage/emulated/0/github/Termux/installs/HPomb.sh
clear;sh /storage/emulated/0/github/Termux/installs/java.sh
clear;sh /storage/emulated/0/github/Termux/installs/Kali.sh
clear;sh /storage/emulated/0/github/Termux/installs/KickThemOut.sh
clear;sh /storage/emulated/0/github/Termux/installs/MariaDB.sh
clear;sh /storage/emulated/0/github/Termux/installs/Metasploit.sh
clear;sh /storage/emulated/0/github/Termux/installs/MOSH.sh
clear;sh /storage/emulated/0/github/Termux/installs/mpd.sh
clear;sh /storage/emulated/0/github/Termux/installs/myserver.sh
clear;sh /storage/emulated/0/github/Termux/installs/Neofetch.sh
clear;sh /storage/emulated/0/github/Termux/installs/oh-my-termux.sh
clear;sh /storage/emulated/0/github/Termux/installs/Oh-My-Zsh.sh
clear;sh /storage/emulated/0/github/Termux/installs/OpenSSH.sh
clear;sh /storage/emulated/0/github/Termux/installs/p10k-Font.sh
clear;sh /storage/emulated/0/github/Termux/installs/Postgresql.sh
clear;sh /storage/emulated/0/github/Termux/installs/PRoot.sh
clear;sh /storage/emulated/0/github/Termux/installs/pyter.sh
clear;sh /storage/emulated/0/github/Termux/installs/Python.sh
clear;sh /storage/emulated/0/github/Termux/installs/pyttsx3.sh
clear;sh /storage/emulated/0/github/Termux/installs/rbenv.sh
clear;sh /storage/emulated/0/github/Termux/installs/rclone.sh
clear;sh /storage/emulated/0/github/Termux/installs/Rsync.sh
clear;sh /storage/emulated/0/github/Termux/installs/Ruby.sh
clear;sh /storage/emulated/0/github/Termux/installs/RVM.sh
clear;sh /storage/emulated/0/github/Termux/installs/services.sh
clear;sh /storage/emulated/0/github/Termux/installs/Setting-up-HTTP-Server.sh
clear;sh /storage/emulated/0/github/Termux/installs/Setting-up-Public-Key-Authentication.sh
clear;sh /storage/emulated/0/github/Termux/installs/setup-pointless-repo.sh
clear;sh /storage/emulated/0/github/Termux/installs/shells.sh
clear;sh /storage/emulated/0/github/Termux/installs/Slack.sh
clear;sh /storage/emulated/0/github/Termux/installs/Snoop.sh
clear;sh /storage/emulated/0/github/Termux/installs/sms.sh
clear;sh /storage/emulated/0/github/Termux/installs/SocialFish.sh
clear;sh /storage/emulated/0/github/Termux/installs/Speak.sh
clear;sh /storage/emulated/0/github/Termux/installs/Speak-Engine.sh
clear;sh /storage/emulated/0/github/Termux/installs/sqlscan.sh
clear;sh /storage/emulated/0/github/Termux/installs/ssh-apt.sh
clear;sh /storage/emulated/0/github/Termux/installs/Sudo.sh
clear;sh /storage/emulated/0/github/Termux/installs/Tool-X.sh
clear;sh /storage/emulated/0/github/Termux/installs/TBomb.sh
clear
sh /storage/emulated/0/github/Termux/installs/Terminal-Look-Awesome-Color-Font-Style.sh
clear
sh /storage/emulated/0/github/Termux/installs/termux-fedora.sh
clear
sh /storage/emulated/0/github/Termux/installs/termux-sms.sh
clear
sh /storage/emulated/0/github/Termux/installs/tor.sh
clear
sh /storage/emulated/0/github/Termux/installs/transmission.sh
clear
sh /storage/emulated/0/github/Termux/installs/ubuntu.sh
clear
sh /storage/emulated/0/github/Termux/installs/xfce4.sh
clear
sh /storage/emulated/0/github/Termux/installs/youtube-dl.sh
clear
sh /storage/emulated/0/github/Termux/installs/Zip.sh
unzip /storage/emulated/0/github/Termux/home/.ssh.zip $HOME/.ssh
cd /storage/emulated/0/github/Termux/
mv -f .git DOTgit
find . -depth -type d -name ".git" -exec rm -rf {} \; && find . -depth -type d -name ".github" -exec rm -rf {} \;
rm -rf /storage/emulated/0/github/Termux/home
cd $HOME/
bash <(curl -fsSL https://git.io/JvMD6)
bash <(curl -fsSL https://git.io/JTgsU)
exit
