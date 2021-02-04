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

echo "\n* Installing Nmap"

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

echo "\n###### Done"

echo "###### Type 'nmap' to start."

echo "\n* Installing RED HAWK"

git clone https://github.com/Tuhinshubhra/RED_HAWK

mv RED_HAWK ~

echo "\n###### Done"

echo "\n* Installing D-Tect"

git clone https://github.com/bibortone/D-Tech

mv D-TECT ~

echo "\n###### Done"

echo "\n* Installing sqlmap"

git clone https://github.com/sqlmapproject/sqlmap

mv sqlmap ~

echo "\n###### Done"

echo "\n* Installing Infoga"

python3 -m pip install requests urllib3 urlparse

git clone https://github.com/m4ll0k/Infoga

mv Infoga ~

echo "\n###### Done"

echo "\n* Installing ReconDog"

git clone https://github.com/UltimateHackers/ReconDog

mv ReconDog ~

echo "\n###### Done"

echo "\n* Installing AndroZenmap"

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh

mkdir -p ~/AndroZenmap

mv androzenmap.sh ~/AndroZenmap

echo "\n###### Done"

echo "\n* Installing sqlmate"

python3 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2

git clone https://github.com/UltimateHackers/sqlmate

mv sqlmate ~

echo "\n###### Done"

echo "\n* Installing AstraNmap"

git clone https://github.com/Gameye98/AstraNmap

mv AstraNmap ~

echo "\n###### Done"

echo "\n* Installing WTF"

python3 -m pip bs4 requests HTMLParser urlparse mechanize argparse

git clone https://github.com/Xi4u7/wtf

mv wtf ~

echo "\n###### Done"

echo "\n* Installing Easymap"

git clone https://github.com/Cvar1984/Easymap

mv Easymap ~

cd ~/Easymap

sh install.sh

echo "\n###### Done"

echo "\n* Installing XD3v"

curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh

mv xd3v.sh ~/../usr/bin/xd3v

chmod +x ~/../usr/bin/xd3v

echo "\n###### Done"

echo "\n###### Type 'xd3v' to start."

echo "\n* Installing Crips"

git clone https://github.com/Manisso/Crips

mv Crips ~

echo "\n###### Done"

echo "\n* Installing SIR"

python3 -m pip install bs4 urllib2

git clone https://github.com/AeonDave/sir.git

mv sir ~

echo "\n###### Done"

echo "\n* Installing Xshell"

git clone https://github.com/Ubaii/Xshell

mv Xshell ~

echo "\n###### Done"

echo "\n* Installing EvilURL"

git clone https://github.com/UndeadSec/EvilURL

mv EvilURL ~

echo "\n###### Done"

echo "\n* Installing Striker"

git clone https://github.com/UltimateHackers/Striker

mv Striker ~

cd ~/Striker

python3 -m pip install -r requirements.txt

echo "\n###### Done"

echo "\n* Installing DSSS"

git clone https://github.com/stamparm/DSSS

mv DSSS ~

echo "\n###### Done"

echo "\n* Installing SQLiv"

git clone https://github.com/Hadesy2k/sqliv

mv sqliv ~

echo "\n###### Done"

echo "\n* Installing sqlscan"

git clone http://www.github.com/Cvar1984/sqlscan

mv sqlscan ~

echo "\n###### Done"

echo "\n* Installing Wordpresscan"

git clone https://github.com/swisskyrepo/Wordpresscan

mv Wordpresscan ~

cd ~/Wordpresscan

python3 -m pip install -r requirements.txt

echo "\n###### Done"

echo "\n* Installing WPScan"

git clone https://github.com/wpscanteam/wpscan

mv wpscan ~

cd ~/wpscan

gem install bundle

bundle config build.nokogiri --use-system-libraries

bundle install

ruby wpscan.rb --update

echo "\n###### Done"

echo "\n* Installing wordpresscan(2)"

git clone https://github.com/silverhat007/termux-wordpresscan

cd termux-wordpresscan

chmod +x *

sh install.sh

mv termux-wordpresscan ~

echo "\n###### Done"

echo "###### Type 'wordpresscan' to start."

echo "\n* Installing Routersploit"

python3 -m pip install requests

cd ..

git clone https://github.com/reverse-shell/routersploit

mv routersploit ~

cd ~/routersploit;python3 -m pip install -r requirements.txt

termux-fix-shebang rsf.py

echo "\n###### Done"

echo "\n* Installing Torshammer"

git clone https://github.com/dotfighter/torshammer

mv torshammer ~

echo "\n###### Done"

echo "\n* Installing Slowloris"

git clone https://github.com/gkbrk/slowloris

mv slowloris ~

echo "\n###### Done"

echo "\n* Installing Fl00d & Fl00d2"

mkdir -p ~/fl00d

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py

mv fl00d.py ~/fl00d

mv fl00d2.py ~/fl00d

echo "\n###### Done"

echo "\n* Installing GoldenEye"

git clone https://github.com/jseidl/GoldenEye

mv GoldenEye ~

echo "\n###### Done"

echo "\n* Installing Xerxes"

git clone https://github.com/zanyarjamal/xerxes

mv xerxes ~

cd ~/xerxes

clang xerxes.c -o xerxes

echo "\n###### Done"

echo "\n* Installing Planetwork-DDOS"

git clone https://github.com/Hydra7/Planetwork-DDOS

mv Planetwork-DDOS ~

echo "\n###### Done"

echo "\n* Installing Hydra"

echo "\n###### Done"

echo "\n* Installing Black Hydra"

git clone https://github.com/Gameye98/Black-Hydra

mv Black-Hydra ~

echo "\n###### Done"

echo "\n* Installing Cupp"

git clone https://github.com/Mebus/cupp

mv cupp ~

echo "\n###### Done"

echo "\n* Installing ASU"

python3 -m pip install requests bs4 mechanize

git clone https://github.com/LOoLzeC/ASU

mv ASU ~

echo "\n###### Done"

echo "\n* Installing Hash-Buster"

git clone https://github.com/UltimateHackers/Hash-Buster

mv Hash-Buster ~

echo "\n###### Done"

echo "\n* Installing InstaHack"

python3 -m pip install requests

git clone https://github.com/avramit/instahack

mv instahack ~

echo "\n###### Done"

echo "\n* Installing indonesian-wordlist"

git clone https://github.com/geovedi/indonesian-wordlist

mv indonesian-wordlist ~

echo "\n###### Done"

echo "\n* Installing Facebook Brute Force 3"

python3 -m pip install mechanize

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py

curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt

mkdir -p ~/facebook-brute-3

mv facebook3.py ~/facebook-brute-3

mv password.txt ~/facebook-brute-3

echo "\n###### Done"

echo "\n* Installing Webdav"

python3 -m pip install urllib3 chardet certifi idna requests

mkdir -p ~/webdav

curl -k -O http://override.waper.co/files/webdav.txt;mv webdav.txt ~/webdav/webdav.py

echo "\n###### Done"

echo "\n* Installing xGans"

mkdir -p ~/xGans

curl -O http://override.waper.co/files/xgans.txt

mv xgans.txt ~/xGans/xgans.py

echo "\n###### Done"

echo "\n* Installing Webdav Mass Exploiter"

python3 -m pip install requests

curl -k -O https://pastebin.com/raw/K1VYVHxX

mv K1VYVHxX webdav.py

mkdir -p ~/webdav-mass-exploit

mv webdav.py ~/webdav-mass-exploit

echo "\n###### Done"

echo "\n* Installing WPSploit"

git clone git clone https://github.com/m4ll0k/wpsploit

mv wpsploit ~

echo "\n###### Done"

echo "\n* Installing sqldump"

python3 -m pip install google

curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py

mkdir -p ~/sqldump

chmod +x sqldump.py

mv sqldump.py ~/sqldump

echo "\n###### Done"

echo "\n* Installing Websploit"

python3 -m pip install scapy

git clone https://github.com/The404Hacking/websploit

mv websploit ~

echo "\n###### Done"

echo "\n* Installing sqlokmed"

python3 -m pip install urllib2

git clone https://github.com/Anb3rSecID/sqlokmed

mv sqlokmed ~

echo "\n###### Done"

echo "\n* Installing zones"

git clone https://github.com/Cvar1984/zones

mv zones ~

echo "\n###### Done"

echo "###### Type 'msfconsole' to start."

echo "\n* Installing Commix"

git clone https://github.com/commixproject/commix

mv commix ~

echo "\n###### Done"

echo "\n* Installing Brutal"

git clone https://github.com/Screetsec/Brutal

mv Brutal ~

echo "\n###### Done"

echo "\n* Installing A-Rat"

git clone https://github.com/Xi4u7/A-Rat

mv A-Rat ~

echo "\n###### Done"

echo "\n* Installing KnockMail"

python3 -m pip install validate_email pyDNS

git clone https://github.com/4w4k3/KnockMail

mv KnockMail ~

echo "\n###### Done"

echo "\n* Installing Spammer-Grab"

python3 -m pip install requests

git clone https://github.com/p4kl0nc4t/spammer-grab

mv spammer-grab ~

echo "\n###### Done"

echo "\n* Installing Hac"

git clone https://github.com/Cvar1984/Hac

mv Hac ~

echo "\n###### Done"

echo "\n* Installing Spammer-Email"

python3 -m pip install argparse requests

git clone https://github.com/p4kl0nc4t/Spammer-Email

mv Spammer-Email ~

echo "\n###### Done"

echo "\n* Installing Rang3r"

python3 -m pip install optparse termcolor

git clone https://github.com/floriankunushevci/rang3r

mv rang3r ~

echo "\n###### Done"

echo "\n* Installing SH33LL"

git clone https://github.com/LOoLzeC/SH33LL

mv SH33LL ~

echo "\n###### Done"

echo "\n* Installing Social-Engineering"

git clone https://github.com/LOoLzeC/social-engineering

mv social-engineering ~

echo "\n###### Done"

echo "\n* Installing SpiderBot"

git clone https://github.com/Cvar1984/SpiderBot

mv SpiderBot ~

echo "\n###### Done"

echo "\n* Installing Ngrok"

git clone https://github.com/themastersunil/ngrok

mv ngrok ~

echo "\n###### Done"

echo "\n* Installing Kali NetHunter"

git clone https://github.com/Hax4us/Nethunter-In-Termux

mv Nethunter-In-Termux ~

echo "\n###### Done"

echo "\n* Installing BlackBox"

python3 -m pip install optparse passlib

git clone https://github.com/jothatron/blackbox

mv blackbox ~

echo "\n###### Done"

echo "\n* Installing XAttacker"

cpnm install HTTP::Request

cpnm install LWP::Useragent

git clone https://github.com/Moham3dRiahi/XAttacker

mv XAttacker ~

echo "\n###### Done"

echo "\n* Installing VCRT"

git clone https://github.com/LOoLzeC/Evil-create-framework

mv Evil-create-framework ~

echo "\n###### Done"

echo "\n* Installing SocialFish"

python3 -m pip install wget

git clone https://github.com/UndeadSec/SocialFish

mv SocialFish ~

echo "\n###### Done"

echo "\n* Installing ECode"

git clone https://github.com/Cvar1984/Ecode

mv Ecode ~

echo "\n###### Done"

echo "\n* Installing Hashzer"

python3 -m pip install requests

git clone https://github.com/Anb3rSecID/Hashzer

mv Hashzer ~

echo "\n###### Done"

echo "\n* Installing XSStrike"

python3 -m pip install fuzzywuzzy prettytable mechanize HTMLParser

git clone https://github.com/UltimateHackers/XSStrike

mv XSStrike ~

echo "\n###### Done"

echo "\n* Installing Breacher"

python3 -m pip install requests argparse

git clone https://github.com/UltimateHackers/Breacher

mv Breacher ~

echo "\n###### Done"

echo "\n* Installing Termux-Styling"

git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script

mv Termux-Styling-Shell-Script ~

echo "\n###### Done"

echo "\n* Installing TXTool"

python3 -m pip install requests

git clone https://github.com/kuburan/txtool

mv txtool ~

echo "\n###### Done"

echo "\n* Installing PassGen"

git clone https://github.com/Cvar1984/PassGen

mv PassGen ~

echo "\n###### Done"

echo "\n* Installing OWScan"

git clone https://github.com/Gameye98/OWScan

mv OWScan ~

echo "\n###### Done"

echo "\n* Installing santet-online"

python3 -m pip install requests

git clone https://github.com/Gameye98/santet-online

mv santet-online ~

echo "\n###### Done"

echo "\n* Installing SpazSMS"

python3 -m pip install requests

git clone https://github.com/Gameye98/SpazSMS

mv SpazSMS ~

echo "\n###### Done"

echo "\n* Installing Hasher"

python3 -m pip install passlib binascii progressbar

git clone https://github.com/ciku370/hasher

mv hasher ~

echo "\n###### Done"

echo "\n* Installing Hash-Generator"

python3 -m pip install passlib progressbar

git clone https://github.com/ciku370/hash-generator

mv hash-generator ~

echo "\n###### Done"

echo "\n* Installing ko-dork"

python3 -m pip install urllib2

git clone https://github.com/ciku370/ko-dork

mv ko-dork ~

echo "\n###### Done"

echo "\n* Installing snitch"

git clone https://github.com/Smaash/snitch

mv snitch ~

echo "\n###### Done"

echo "\n* Installing OSIF"

python3 -m pip install requests

git clone https://github.com/ciku370/OSIF

mv OSIF ~

echo "\n###### Done"

echo "\n* Installing Devploit"

python3 -m pip install urllib2

git clone https://github.com/joker25000/Devploit

mv Devploit ~

echo "\n###### Done"

echo "\n* Installing Hasherdotid"

git clone https://github.com/galauerscrew/hasherdotid

mv hasherdotid ~

echo "\n###### Done"

echo "\n* Installing Namechk"

git clone https://github.com/HA71/Namechk

mv Namechk ~

echo "\n###### Done"

echo "\n* Installing xl-py"

git clone https://github.com/albertoanggi/xl-py

mv xl-py ~

echo "\n###### Done"

echo "\n* Installing Beanshell"

wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb

dpkg -i beanshell_2.04_all.deb

rm -rf beanshell_2.04_all.deb

echo "\n###### Done"

echo "###### Type 'bsh' to start."

echo "\n* Installing MSF-Pg"

git clone https://github.com/haxzsadik/MSF-Pg

mv MSF-Pg ~

echo "###### Done"

echo "\n* Installing Crunch"

echo "###### Done"

echo "###### Type 'crunch' to start."

echo "\n* Installing WebConn"

git clone https://github.com/SkyKnight-Team/WebConn

mv WebConn ~

echo "###### Done"

echo "\n* Installing Binary Exploitation"

echo "###### Done"

echo "###### Tutorial: https://youtu.be/3NTXFUxcKPc"

echo "\n* Installing Textr"

wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb

dpkg -i textr_1.0_all.deb

rm -rf textr_1.0_all.deb

echo "\n###### Done"

echo "###### Type 'textr' to start."

echo "\n* Installing ApSca"

wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb

dpkg -i apsca_0.1_all.deb

rm -rf apsca_0.1_all.deb

echo "\n###### Done"

echo "###### Type 'apsca' to start."

echo "\n* Installing amox"

wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb

dpkg -i amox_1.0_all.deb

rm -rf amox_1.0_all.deb

echo "\n###### Done"

echo "###### Type 'amox' to start."

echo "\n* Installing FaDe"

python3 -m pip install requests

git clone https://github.com/Gameye98/FaDe

mv FaDe ~

echo "\n###### Done"

echo "\n* Installing GINF"

git clone https://github.com/Gameye98/GINF

mv GINF ~

echo "\n###### Done"

echo "\n* Installing AUXILE"

python3 -m pip install requests bs4 pexpect

git clone https://github.com/CiKu370/AUXILE

mv AUXILE ~

echo "\n###### Done"

echo "\n* Installing inther"

git clone https://github.com/Gameye98/inther

mv inther ~

echo "\n###### Done"

echo "\n* Installing HPB"

wget https://raw.githubusercontent.com/Cvar1984/HPB/master/html_0.1_all.deb

dpkg -i html_0.1_all.deb

rm -rf html_0.1_all.deb

echo "\n###### Done"

echo "###### Type 'hpb' to start."

echo "\n* Installing FMBrute"

python -m pip install requests

git clone https://github.com/BlackHoleSecurity/FMBrute

mv FMBrute ~

echo "\n###### Done"

echo "\n* Installing HashID"

python3 -m pip install hashid

echo "###### Done"

echo "###### Type 'hashid -h' to show usage of hashid"

echo "\n* Installing GPS Tracking"

git clone https://github.com/indosecid/gps_tracking

mv gps_tracking ~

echo "###### Done"

echo "\n* Installing PRET"

python3 -m pip install colorama pysnmp

git clone https://github.com/RUB-NDS/PRET

mv PRET ~

echo "###### Done"

echo "\n* Installing AutoVisitor"

git clone https://github.com/wannabeee/AutoVisitor

mv AutoVisitor ~

echo "###### Done"

echo "\n* Installing Atlas"

python3 -m pip install urllib2

git clone https://github.com/m4ll0k/Atlas

mv Atlas ~

echo "###### Done"

echo "\n* Installing Hashcat"

echo "###### Done"

echo "###### Type 'hashcat' to start."

echo "\n* Installing LiteOTP"

wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite

echo "###### Done"

echo "###### Type 'lite' to start."

echo "\n* Installing FBBrute"

python -m pip install requests

git clone https://github.com/Gameye98/FBBrute

mv FBBrute ~

echo "\n###### Done"

echo "\n* Installing fim"

python -m pip install requests bs4

git clone https://github.com/karjok/fim

mv fim ~

echo "\n###### Done"

echo "\n* Installing RShell"

python -m pip install colorama

git clone https://github.com/Jishu-Epic/RShell

mv RShell ~

echo "\n###### Done"

echo "\n* Installing TermPyter"

git clone https://github.com/Jishu-Epic/TermPyter

mv TermPyter ~

echo "\n###### Done"

echo "\n* Installing MaxSubdoFinder"

python3 -m pip install requests

git clone https://github.com/maxteroit/MaxSubdoFinder

mv MaxSubdoFinder ~

echo "\n###### Done"

echo "\n* Installing jadx"

wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true

dpkg -i jadx-0.6.1_all.deb?raw=true

rm -rf jadx-0.6.1_all.deb?raw=true

echo "\n###### Done"
