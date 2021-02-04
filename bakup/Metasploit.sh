#!/data/data/com.termux/files/usr/bin/sh

echo "\nMetasploit Install"

echo "\nRemove Old Folder if exist"

find $HOME -name "metasploit*" -type d -exec rm -rf {} \;

cd /data/data/com.termux/files/home/

cwd=$(pwd)
msfvar=5.0.83
msfpath='/data/data/com.termux/files/home'

apt install -y libiconv

apt install -y zlib

apt install -y autoconf

apt install -y bison

apt install -y clang

apt install -y coreutils

apt install -y curl

apt install -y findutils

apt install -y git

apt install -y apr

apt install -y apr-util

apt install -y libffi

apt install -y libgmp

apt install -y libpcap

apt install -y postgresql

apt install -y readline

apt install -y libsqlite

apt install -y openssl

apt install -y libtool

apt install -y libxml2

apt install -y libxslt

apt install -y ncurses

apt install -y pkg-config

apt install -y wget

apt install -y make

apt install -y ruby

apt install -y libgrpc

apt install -y termux-tools

apt install -y ncurses-utils

apt install -y ncurses

apt install -y unzip

apt install -y zip

apt install -y tar

apt install -y termux-elf-cleaner

echo "\nMany phones are claiming libxml2 not found error"

ln -sf $PREFIX/include/libxml2/libxml $PREFIX/include/

cd $msfpath

curl -LO https://github.com/rapid7/metasploit-framework/archive/$msfvar.tar.gz

tar -xf $msfpath/$msfvar.tar.gz

mv $msfpath/metasploit-framework-$msfvar $msfpath/metasploit-framework

cd $msfpath/metasploit-framework

echo "\nUpdate rubygems-update"

if [ "$(gem list -i rubygems-update 2>/dev/null)" = "false" ]; then
	gem install --no-document --verbose rubygems-update
fi

echo "\nUpdate rubygems"

update_rubygems

echo "\nInstall bundler"

gem install --no-document --verbose bundler:1.17.3

echo "\nInstalling all gems"

bundle config build.nokogiri --use-system-libraries

bundle install -j3

echo "\nGems installed"

echo "\nSome fixes"

sed -i "s@/etc/resolv.conf@$PREFIX/etc/resolv.conf@g" $msfpath/metasploit-framework/lib/net/dns/resolver.rb

find "$msfpath"/metasploit-framework -type f -executable -print0 | xargs -0 -r termux-fix-shebang

find "$PREFIX"/lib/ruby/gems -type f -iname \*.so -print0 | xargs -0 -r termux-elf-cleaner

echo "\nCreating database"

mkdir -p $msfpath/metasploit-framework/config && cd $msfpath/metasploit-framework/config

curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/database.yml

mkdir -p $PREFIX/var/lib/postgresql

pg_ctl -D "$PREFIX"/var/lib/postgresql stop > /dev/null 2>&1 || true

if ! pg_ctl -D "$PREFIX"/var/lib/postgresql start --silent; then
    initdb "$PREFIX"/var/lib/postgresql
    pg_ctl -D "$PREFIX"/var/lib/postgresql start --silent
fi

if [ -z "$(psql postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='msf'")" ]; then
    createuser msf
fi

if [ -z "$(psql -l | grep msf_database)" ]; then
    createdb msf_database
fi

rm $msfpath/$msfvar.tar.gz

cd ${PREFIX}/bin && curl -LO https://hax4us.github.io/files/msfconsole && chmod +x msfconsole

ln -sf $(which msfconsole) $PREFIX/bin/msfvenom

echo "\nyou can directly use msfvenom or msfconsole rather than ./msfvenom or ./msfconsole."
