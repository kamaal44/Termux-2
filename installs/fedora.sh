#!/data/data/com.termux/files/usr/bin/bash

echo "\nFedora Install"

echo "\ninput validator and help"

case "$1" in
	f31_arm64)
	    DOCKERIMAGE=https://download.fedoraproject.org/pub/fedora/linux/releases/31/Container/aarch64/images/Fedora-Container-Base-31-1.9.aarch64.tar.xz
	    ;;
        f32_arm64)
	    DOCKERIMAGE=https://download.fedoraproject.org/pub/fedora/linux/releases/32/Container/aarch64/images/Fedora-Container-Base-32-1.6.aarch64.tar.xz
	    ;;
#	uninstall)
#	    chmod -R 777 /data/data/com.termux/files/home/fedora
#	    rm -rf /data/data/com.termux/files/home/fedora
#	    exit 0
#	    ;;
	*)
	    echo $"Usage: $0 {f31_arm64|f32_arm64|uninstall}"
	    exit 2
	    ;;
esac


# install necessary packages

pkg install proot tar wget -y

# get the docker image

mkdir /data/data/com.termux/files/home/fedora

cd /data/data/com.termux/files/home/fedora

/data/data/com.termux/files/usr/bin/wget $DOCKERIMAGE -O fedora.tar.xz

# extract the Docker image

/data/data/com.termux/files/usr/bin/tar xvf fedora.tar.xz --strip-components=1 --exclude json --exclude VERSION

# extract the rootfs

/data/data/com.termux/files/usr/bin/tar xpf layer.tar

# cleanup

chmod +w .

rm -rf layer.tar

rm -rf fedora.tar.xz

# fix DNS

echo "nameserver 8.8.8.8" > /data/data/com.termux/files/home/fedora/etc/resolv.conf

# make a shortcut

cat > /data/data/com.termux/files/usr/bin/startfedora <<- EOM

#!/data/data/com.termux/files/usr/bin/bash

unset LD_PRELOAD && proot --link2symlink -0 -r /data/data/com.termux/files/home/fedora -b /dev/ -b /sys/ -b /proc/ -b /storage/ -b /data/data/com.termux/files/home/ -w /data/data/com.termux/files/home/ /bin/env -i HOME=/root TERM="$TERM" PS1='[termux@fedora \W]\$ ' LANG=$LANG PATH=/bin:/usr/bin:/sbin:/usr/sbin /bin/bash --login
EOM

chmod +x /data/data/com.termux/files/usr/bin/startfedora

echo "All done! Start Fedora with 'startfedora'. Get updates with regular 'dnf update'. "
