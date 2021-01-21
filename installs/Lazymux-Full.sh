#!/system/bin/sh

# Lazymux Complete Install
# ========================

echo "

 /\ \                                                            
 \ \ \         __     ____    __  __    ___ ___   __  __  __  _  
  \ \ \  __  /"__`\  /\_ ,`\ /\ \/\ \ /" __` __`\/\ \/\ \/\ \/"\ 
   \ \ \L\ \/\ \L\.\_\/_/  /_\ \ \_\ \/\ \/\ \/\ \ \ \_\ \/>  </ 
    \ \____/\ \__/.\_\ /\____\\/`____ \ \_\ \_\ \_\ \____//\_/\_\
     \/___/  \/__/\/_/ \/____/ `/___/> \/_/\/_/\/_/\/___/ \//\/_/
                                    /\___/                         
                                    \/__/

                Created by weilerwebservices@gmail.com

"

apt update -y

apt upgrade -y

echo -e "\n* Installing Nmap"

apt install -y nmap

apt install -y git

apt install -y python

apt install -y curl

apt install -y php

apt install -y python-dev

apt install -y libxml2-dev

apt install -y libxml2-utils

apt install -y libxslt-dev

apt install -y lynx

apt install -y figlet

apt install -y ruby

apt install -y nano

apt install -y w3m

apt install -y clang

apt install -y hydra

apt install -y openssl

apt install -y libcurl

apt install -y wget

apt install -y perl

apt install -y ruby

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

echo -e "\n###### Done"

echo "###### Type 'nmap' to start."

echo -e "\n* Installing RED HAWK"

git clone https://github.com/Tuhinshubhra/RED_HAWK

mv RED_HAWK ~

echo -e "\n###### Done"

echo -e "\n* Installing D-Tect"

git clone https://github.com/bibortone/D-Tech

mv D-TECT ~

echo -e "\n###### Done"

echo -e "\n* Installing sqlmap"

git clone https://github.com/sqlmapproject/sqlmap

mv sqlmap ~

echo -e "\n###### Done"

echo -e "\n* Installing Infoga"

python3 -m pip install requests urllib3 urlparse

git clone https://github.com/m4ll0k/Infoga

mv Infoga ~

echo -e "\n###### Done"

echo -e "\n* Installing ReconDog"

git clone https://github.com/UltimateHackers/ReconDog

mv ReconDog ~

echo -e "\n###### Done"

echo -e "\n* Installing AndroZenmap"

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh

mkdir -p ~/AndroZenmap

mv androzenmap.sh ~/AndroZenmap

echo -e "\n###### Done"

echo -e "\n* Installing sqlmate"

python3 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2

git clone https://github.com/UltimateHackers/sqlmate

mv sqlmate ~

echo -e "\n###### Done"

echo -e "\n* Installing AstraNmap"

git clone https://github.com/Gameye98/AstraNmap

mv AstraNmap ~

echo -e "\n###### Done"

echo -e "\n* Installing WTF"

python3 -m pip bs4 requests HTMLParser urlparse mechanize argparse

git clone https://github.com/Xi4u7/wtf

mv wtf ~

echo -e "\n###### Done"

echo -e "\n* Installing Easymap"

git clone https://github.com/Cvar1984/Easymap

mv Easymap ~

cd ~/Easymap

sh install.sh

echo -e "\n###### Done"

echo -e "\n* Installing XD3v"

curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh

mv xd3v.sh ~/../usr/bin/xd3v

chmod +x ~/../usr/bin/xd3v

echo -e "\n###### Done"

echo -e "\n###### Type 'xd3v' to start."

echo -e "\n* Installing Crips"

git clone https://github.com/Manisso/Crips

mv Crips ~

echo -e "\n###### Done"

echo -e "\n* Installing SIR"

python3 -m pip install bs4 urllib2

git clone https://github.com/AeonDave/sir.git

mv sir ~

echo -e "\n###### Done"

echo -e "\n* Installing Xshell"

git clone https://github.com/Ubaii/Xshell

mv Xshell ~

echo -e "\n###### Done"

echo -e "\n* Installing EvilURL"

git clone https://github.com/UndeadSec/EvilURL

mv EvilURL ~

echo -e "\n###### Done"

echo -e "\n* Installing Striker"

git clone https://github.com/UltimateHackers/Striker

mv Striker ~

cd ~/Striker

python3 -m pip install -r requirements.txt

echo -e "\n###### Done"

echo -e "\n* Installing DSSS"

git clone https://github.com/stamparm/DSSS

mv DSSS ~

echo -e "\n###### Done"

echo -e "\n* Installing SQLiv"

git clone https://github.com/Hadesy2k/sqliv

mv sqliv ~

echo -e "\n###### Done"

echo -e "\n* Installing sqlscan"

git clone http://www.github.com/Cvar1984/sqlscan

mv sqlscan ~

echo -e "\n###### Done"

echo -e "\n* Installing Wordpresscan"

git clone https://github.com/swisskyrepo/Wordpresscan

mv Wordpresscan ~

cd ~/Wordpresscan

python3 -m pip install -r requirements.txt

echo -e "\n###### Done"

echo -e "\n* Installing WPScan"

git clone https://github.com/wpscanteam/wpscan

mv wpscan ~

cd ~/wpscan

gem install bundle

bundle config build.nokogiri --use-system-libraries

bundle install

ruby wpscan.rb --update

echo -e "\n###### Done"

echo -e "\n* Installing wordpresscan(2)"

git clone https://github.com/silverhat007/termux-wordpresscan

cd termux-wordpresscan

chmod +x *

sh install.sh

mv termux-wordpresscan ~

echo -e "\n###### Done"

echo "###### Type 'wordpresscan' to start."

echo -e "\n* Installing Routersploit"

python3 -m pip install requests

cd ..

git clone https://github.com/reverse-shell/routersploit

mv routersploit ~

cd ~/routersploit;python3 -m pip install -r requirements.txt

termux-fix-shebang rsf.py

echo -e "\n###### Done"

echo -e "\n* Installing Torshammer"

git clone https://github.com/dotfighter/torshammer

mv torshammer ~

echo -e "\n###### Done"

echo -e "\n* Installing Slowloris"

git clone https://github.com/gkbrk/slowloris

mv slowloris ~

echo -e "\n###### Done"

echo -e "\n* Installing Fl00d & Fl00d2"

mkdir -p ~/fl00d

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py

mv fl00d.py ~/fl00d

mv fl00d2.py ~/fl00d

echo -e "\n###### Done"

echo -e "\n* Installing GoldenEye"

git clone https://github.com/jseidl/GoldenEye

mv GoldenEye ~

echo -e "\n###### Done"

echo -e "\n* Installing Xerxes"

git clone https://github.com/zanyarjamal/xerxes

mv xerxes ~

cd ~/xerxes

clang xerxes.c -o xerxes

echo -e "\n###### Done"

echo -e "\n* Installing Planetwork-DDOS"

git clone https://github.com/Hydra7/Planetwork-DDOS

mv Planetwork-DDOS ~

echo -e "\n###### Done"

echo -e "\n* Installing Hydra"

echo -e "\n###### Done"

echo -e "\n* Installing Black Hydra"

git clone https://github.com/Gameye98/Black-Hydra

mv Black-Hydra ~

echo -e "\n###### Done"

echo -e "\n* Installing Cupp"

git clone https://github.com/Mebus/cupp

mv cupp ~

echo -e "\n###### Done"

echo -e "\n* Installing ASU"

python3 -m pip install requests bs4 mechanize

git clone https://github.com/LOoLzeC/ASU

mv ASU ~

echo -e "\n###### Done"

echo -e "\n* Installing Hash-Buster"

git clone https://github.com/UltimateHackers/Hash-Buster

mv Hash-Buster ~

echo -e "\n###### Done"

echo -e "\n* Installing InstaHack"

python3 -m pip install requests

git clone https://github.com/avramit/instahack

mv instahack ~

echo -e "\n###### Done"

echo -e "\n* Installing indonesian-wordlist"

git clone https://github.com/geovedi/indonesian-wordlist

mv indonesian-wordlist ~

echo -e "\n###### Done"

echo -e "\n* Installing Facebook Brute Force 3"

python3 -m pip install mechanize

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt

mkdir -p ~/facebook-brute-3

mv facebook3.py ~/facebook-brute-3

mv password.txt ~/facebook-brute-3

echo -e "\n###### Done"

echo -e "\n* Installing Webdav"

python3 -m pip install urllib3 chardet certifi idna requests

mkdir -p ~/webdav

curl -k -O http://override.waper.co/files/webdav.txt;mv webdav.txt ~/webdav/webdav.py

echo -e "\n###### Done"

echo -e "\n* Installing xGans"

mkdir -p ~/xGans

curl -O http://override.waper.co/files/xgans.txt

mv xgans.txt ~/xGans/xgans.py

echo -e "\n###### Done"

echo -e "\n* Installing Webdav Mass Exploiter"

python3 -m pip install requests

curl -k -O https://pastebin.com/raw/K1VYVHxX

mv K1VYVHxX webdav.py

mkdir -p ~/webdav-mass-exploit

mv webdav.py ~/webdav-mass-exploit

echo -e "\n###### Done"

echo -e "\n* Installing WPSploit"

git clone git clone https://github.com/m4ll0k/wpsploit

mv wpsploit ~

echo -e "\n###### Done"

echo -e "\n* Installing sqldump"

python3 -m pip install google

curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py

mkdir -p ~/sqldump

chmod +x sqldump.py

mv sqldump.py ~/sqldump

echo -e "\n###### Done"

echo -e "\n* Installing Websploit"

python3 -m pip install scapy

git clone https://github.com/The404Hacking/websploit

mv websploit ~

echo -e "\n###### Done"

echo -e "\n* Installing sqlokmed"

python3 -m pip install urllib2

git clone https://github.com/Anb3rSecID/sqlokmed

mv sqlokmed ~

echo -e "\n###### Done"

echo -e "\n* Installing zones"

git clone https://github.com/Cvar1984/zones

mv zones ~

echo -e "\n###### Done"

echo "###### Type 'msfconsole' to start."

echo -e "\n* Installing Commix"

git clone https://github.com/commixproject/commix

mv commix ~

echo -e "\n###### Done"

echo -e "\n* Installing Brutal"

git clone https://github.com/Screetsec/Brutal

mv Brutal ~

echo -e "\n###### Done"

echo -e "\n* Installing A-Rat"

git clone https://github.com/Xi4u7/A-Rat

mv A-Rat ~

echo -e "\n###### Done"

echo -e "\n* Installing KnockMail"

python3 -m pip install validate_email pyDNS

git clone https://github.com/4w4k3/KnockMail

mv KnockMail ~

echo -e "\n###### Done"

echo -e "\n* Installing Spammer-Grab"

python3 -m pip install requests

git clone https://github.com/p4kl0nc4t/spammer-grab

mv spammer-grab ~

echo -e "\n###### Done"

echo -e "\n* Installing Hac"

git clone https://github.com/Cvar1984/Hac

mv Hac ~

echo -e "\n###### Done"

echo -e "\n* Installing Spammer-Email"

python3 -m pip install argparse requests

git clone https://github.com/p4kl0nc4t/Spammer-Email

mv Spammer-Email ~

echo -e "\n###### Done"

echo -e "\n* Installing Rang3r"

python3 -m pip install optparse termcolor

git clone https://github.com/floriankunushevci/rang3r

mv rang3r ~

echo -e "\n###### Done"

echo -e "\n* Installing SH33LL"

git clone https://github.com/LOoLzeC/SH33LL

mv SH33LL ~

echo -e "\n###### Done"

echo -e "\n* Installing Social-Engineering"

git clone https://github.com/LOoLzeC/social-engineering

mv social-engineering ~

echo -e "\n###### Done"

echo -e "\n* Installing SpiderBot"

git clone https://github.com/Cvar1984/SpiderBot

mv SpiderBot ~

echo -e "\n###### Done"

echo -e "\n* Installing Ngrok"

git clone https://github.com/themastersunil/ngrok

mv ngrok ~

echo -e "\n###### Done"

echo -e "\n* Installing Kali NetHunter"

git clone https://github.com/Hax4us/Nethunter-In-Termux

mv Nethunter-In-Termux ~

echo -e "\n###### Done"

echo -e "\n* Installing BlackBox"

python3 -m pip install optparse passlib

git clone https://github.com/jothatron/blackbox

mv blackbox ~

echo -e "\n###### Done"

echo -e "\n* Installing XAttacker"

cpnm install HTTP::Request

cpnm install LWP::Useragent

git clone https://github.com/Moham3dRiahi/XAttacker

mv XAttacker ~

echo -e "\n###### Done"

echo -e "\n* Installing VCRT"

git clone https://github.com/LOoLzeC/Evil-create-framework

mv Evil-create-framework ~

echo -e "\n###### Done"

echo -e "\n* Installing SocialFish"

python3 -m pip install wget

git clone https://github.com/UndeadSec/SocialFish

mv SocialFish ~

echo -e "\n###### Done"

echo -e "\n* Installing ECode"

git clone https://github.com/Cvar1984/Ecode

mv Ecode ~

echo -e "\n###### Done"

echo -e "\n* Installing Hashzer"

python3 -m pip install requests

git clone https://github.com/Anb3rSecID/Hashzer

mv Hashzer ~

echo -e "\n###### Done"

echo -e "\n* Installing XSStrike"

python3 -m pip install fuzzywuzzy prettytable mechanize HTMLParser

git clone https://github.com/UltimateHackers/XSStrike

mv XSStrike ~

echo -e "\n###### Done"

echo -e "\n* Installing Breacher"

python3 -m pip install requests argparse

git clone https://github.com/UltimateHackers/Breacher

mv Breacher ~

echo -e "\n###### Done"

echo -e "\n* Installing Termux-Styling"

git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script

mv Termux-Styling-Shell-Script ~

echo -e "\n###### Done"

echo -e "\n* Installing TXTool"

python3 -m pip install requests

git clone https://github.com/kuburan/txtool

mv txtool ~

echo -e "\n###### Done"

echo -e "\n* Installing PassGen"

git clone https://github.com/Cvar1984/PassGen

mv PassGen ~

echo -e "\n###### Done"

echo -e "\n* Installing OWScan"

git clone https://github.com/Gameye98/OWScan

mv OWScan ~

echo -e "\n###### Done"

echo -e "\n* Installing santet-online"

python3 -m pip install requests

git clone https://github.com/Gameye98/santet-online

mv santet-online ~

echo -e "\n###### Done"

echo -e "\n* Installing SpazSMS"

python3 -m pip install requests

git clone https://github.com/Gameye98/SpazSMS

mv SpazSMS ~

echo -e "\n###### Done"

echo -e "\n* Installing Hasher"

python3 -m pip install passlib binascii progressbar

git clone https://github.com/ciku370/hasher

mv hasher ~

echo -e "\n###### Done"

echo -e "\n* Installing Hash-Generator"

python3 -m pip install passlib progressbar

git clone https://github.com/ciku370/hash-generator

mv hash-generator ~

echo -e "\n###### Done"

echo -e "\n* Installing ko-dork"

python3 -m pip install urllib2

git clone https://github.com/ciku370/ko-dork

mv ko-dork ~

echo -e "\n###### Done"

echo -e "\n* Installing snitch"

git clone https://github.com/Smaash/snitch

mv snitch ~

echo -e "\n###### Done"

echo -e "\n* Installing OSIF"

python3 -m pip install requests

git clone https://github.com/ciku370/OSIF

mv OSIF ~

echo -e "\n###### Done"

echo -e "\n* Installing Devploit"

python3 -m pip install urllib2

git clone https://github.com/joker25000/Devploit

mv Devploit ~

echo -e "\n###### Done"

echo -e "\n* Installing Hasherdotid"

git clone https://github.com/galauerscrew/hasherdotid

mv hasherdotid ~

echo -e "\n###### Done"

echo -e "\n* Installing Namechk"

git clone https://github.com/HA71/Namechk

mv Namechk ~

echo -e "\n###### Done"

echo -e "\n* Installing xl-py"

git clone https://github.com/albertoanggi/xl-py

mv xl-py ~

echo -e "\n###### Done"

echo -e "\n* Installing Beanshell"

wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb

dpkg -i beanshell_2.04_all.deb

rm -rf beanshell_2.04_all.deb

echo -e "\n###### Done"

echo "###### Type 'bsh' to start."

echo -e "\n* Installing MSF-Pg"

git clone https://github.com/haxzsadik/MSF-Pg

mv MSF-Pg ~

echo "###### Done"

echo -e "\n* Installing Crunch"

echo "###### Done"

echo "###### Type 'crunch' to start."

echo -e "\n* Installing WebConn"

git clone https://github.com/SkyKnight-Team/WebConn

mv WebConn ~

echo "###### Done"

echo -e "\n* Installing Binary Exploitation"

echo "###### Done"

echo "###### Tutorial: https://youtu.be/3NTXFUxcKPc"

echo -e "\n* Installing Textr"

wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb

dpkg -i textr_1.0_all.deb

rm -rf textr_1.0_all.deb

echo -e "\n###### Done"

echo "###### Type 'textr' to start."

echo -e "\n* Installing ApSca"

wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb

dpkg -i apsca_0.1_all.deb

rm -rf apsca_0.1_all.deb

echo -e "\n###### Done"

echo "###### Type 'apsca' to start."

echo -e "\n* Installing amox"

wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb

dpkg -i amox_1.0_all.deb

rm -rf amox_1.0_all.deb

echo -e "\n###### Done"

echo "###### Type 'amox' to start."

echo -e "\n* Installing FaDe"

python3 -m pip install requests

git clone https://github.com/Gameye98/FaDe

mv FaDe ~

echo -e "\n###### Done"

echo -e "\n* Installing GINF"

git clone https://github.com/Gameye98/GINF

mv GINF ~

echo -e "\n###### Done"

echo -e "\n* Installing AUXILE"

python3 -m pip install requests bs4 pexpect

git clone https://github.com/CiKu370/AUXILE

mv AUXILE ~

echo -e "\n###### Done"

echo -e "\n* Installing inther"

git clone https://github.com/Gameye98/inther

mv inther ~

echo -e "\n###### Done"

echo -e "\n* Installing HPB"

wget https://raw.githubusercontent.com/Cvar1984/HPB/master/html_0.1_all.deb

dpkg -i html_0.1_all.deb

rm -rf html_0.1_all.deb

echo -e "\n###### Done"

echo "###### Type 'hpb' to start."

echo -e "\n* Installing FMBrute"

python -m pip install requests

git clone https://github.com/BlackHoleSecurity/FMBrute

mv FMBrute ~

echo -e "\n###### Done"

echo -e "\n* Installing HashID"

python3 -m pip install hashid

echo "###### Done"

echo "###### Type 'hashid -h' to show usage of hashid"

echo -e "\n* Installing GPS Tracking"

git clone https://github.com/indosecid/gps_tracking

mv gps_tracking ~

echo "###### Done"

echo -e "\n* Installing PRET"

python3 -m pip install colorama pysnmp

git clone https://github.com/RUB-NDS/PRET

mv PRET ~

echo "###### Done"

echo -e "\n* Installing AutoVisitor"

git clone https://github.com/wannabeee/AutoVisitor

mv AutoVisitor ~

echo "###### Done"

echo -e "\n* Installing Atlas"

python3 -m pip install urllib2

git clone https://github.com/m4ll0k/Atlas

mv Atlas ~

echo "###### Done"

echo -e "\n* Installing Hashcat"

echo "###### Done"

echo "###### Type 'hashcat' to start."

echo -e "\n* Installing LiteOTP"

wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite

echo "###### Done"

echo "###### Type 'lite' to start."

echo -e "\n* Installing FBBrute"

python -m pip install requests

git clone https://github.com/Gameye98/FBBrute

mv FBBrute ~

echo -e "\n###### Done"

echo -e "\n* Installing fim"

python -m pip install requests bs4

git clone https://github.com/karjok/fim

mv fim ~

echo -e "\n###### Done"

echo -e "\n* Installing RShell"

python -m pip install colorama

git clone https://github.com/Jishu-Epic/RShell

mv RShell ~

echo -e "\n###### Done"

echo -e "\n* Installing TermPyter"

git clone https://github.com/Jishu-Epic/TermPyter

mv TermPyter ~

echo -e "\n###### Done"

echo -e "\n* Installing MaxSubdoFinder"

python3 -m pip install requests

git clone https://github.com/maxteroit/MaxSubdoFinder

mv MaxSubdoFinder ~

echo -e "\n###### Done"

echo -e "\n* Installing jadx"

wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true

dpkg -i jadx-0.6.1_all.deb?raw=true

rm -rf jadx-0.6.1_all.deb?raw=true

echo -e "\n###### Done"
