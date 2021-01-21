#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nSetup Pointless Repo"

echo -e "\nGet some needed tools. coreutils for mkdir command, gnugp for the signing key, and apt-transport-https to actually connect to the repo"

echo -e "\nUpdate apt"

apt update -y

apt --assume-yes upgrade

apt --assume-yes install coreutils gnupg

echo -e "\nMake the sources.list.d directory"

mkdir -p $PREFIX/etc/apt/sources.list.d

echo -e "\nWrite the needed source file"

if apt-cache policy | grep -q "termux.*24\|termux.org\|bintray.*24" ; then

echo "deb https://its-pointless.github.io/files/24 termux extras" > $PREFIX/etc/apt/sources.list.d/pointless.list
else
echo "deb https://its-pointless.github.io/files/21 termux extras" > $PREFIX/etc/apt/sources.list.d/pointless.list
fi

echo -e "\nAdd signing key from https://its-pointless.github.io/pointless.gpg"

if [ -n $(command -v curl) ]; then
curl -sL https://its-pointless.github.io/pointless.gpg | apt-key add -
elif [ -n $(command -v wget) ]; then
wget -qO - https://its-pointless.github.io/pointless.gpg | apt-key add -
fi
