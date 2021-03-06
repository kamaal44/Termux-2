#!/data/data/com.termux/files/usr/bin/bash

echo "\nTermux Slack Install"

echo "\nThis setup script will attempt to set Slackware Linux up in your Termux environment."

echo "\nWhen successfully completed, you will be at the bash prompt in Slackware Linux in Termux."

pkg update -y

pkg upgrade -y

pkg install -y proot tar wget curl

mkdir -p $HOME/slackware

cd $HOME/slackware

echo "\nDownloading slackware-image."

MINIROOTFS_VERSION=$(curl https://slackware.uk/slackwarearm/slackwarearm-devtools/minirootfs/roots/ | grep ">slack-current-miniroot_.*\.tar.xz" -o | grep -o "[0-9].*[0-9]")

if [ "$(uname -m)" = "aarch64" ] || [ "$(uname -m)" = "armv7l" ];then
    wget -c ftp://ftp.arm.slackware.com/slackwarearm/slackwarearm-devtools/minirootfs/roots/slack-current-miniroot_${MINIROOTFS_VERSION}.tar.xz -O slack-current-miniroot_${MINIROOTFS_VERSION}.tar.xz
else
    echo "\nUnknown architecture version for this setup script! There is hope."
    echo "\nPlease check for other available architectures at http://mirror.archlinuxarm.org/os/"
    exit 1
fi

proot --link2symlink tar -xvf slack-current-miniroot_${MINIROOTFS_VERSION}.tar.xz --exclude=dev||:

echo "\nConfiguring Slackware"

mv $HOME/slackware/etc/resolv.conf $HOME/slackware/etc/resolv.conf.orig

cat <<EOF > $HOME/slackware/etc/resolv.conf
nameserver 1.1.1.1
nameserver 8.8.8.8
nameserver 8.8.4.4
EOF

bin=startSlackware

echo "\nWriting launch script."

cat > $bin <<- EOM

#!/data/data/com.termux/files/usr/bin/bash

unset LD_PRELOAD

proot --link2symlink -0 -r ~/slackware -b /dev/ -b /sys/ -b /proc/ -b /storage/ -b $HOME -w $HOME /bin/env -i HOME=/root TERM="$TERM" PS1='[termux@slackware \W]\$ ' LANG=$LANG PATH=/bin:/usr/bin:/sbin:/usr/sbin /bin/bash --login
EOM

echo "\nMaking $bin executable."

chmod 700 $bin

echo "\nLaunch Slackware Linux in Termux with ./slackware/$bin"

$HOME/slackware/$bin
