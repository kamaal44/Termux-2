#!/data/data/com.termux/files/usr/bin/bash

echo
echo "Starting ..."
echo
sleep 2

apt -y update
apt -y upgrade
apt -y install clang
apt -y install nano
apt -y install vim 
apt -y install less
apt -y install coreutils
apt -y install diffutils
apt -y install perl
apt -y install sed
apt -y install tar
apt -y install lynx
apt -y install grep
apt -y install ncurses-utils
apt -y install proot
apt -y clean

cd
curl -O https://utopia.duth.gr/glykos/linux/android.tar
tar xvf android.tar
rm android.tar
mv android.sh data/.android.sh
mkdir -p termux
cp -r .bashrc .termux data progs termux/
termux-reload-settings

if ! grep -q /home/termux "/data/data/com.termux/files/usr/bin/termux-chroot"; then
    sed -i 's/=\/home/=\/home\/termux/g' /data/data/com.termux/files/usr/bin/termux-chroot
fi

echo 
echo 
echo "All done."
echo
echo

