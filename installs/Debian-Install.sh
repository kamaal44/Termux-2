#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nDebian Install"

pkg install -y debootstrap proot wget

cd /sdcard/github/Termux/installs/

uname -m

debootstrap --arch=ARCH stable debian-stable http://ftp.debian.org/debian/ 

echo -e "\nARCH is arm64 for aarch64, etc."

echo -e "\nThen setup proot to mount the container."

echo -e "\nA sample proot start.sh includes"

#!/data/data/com.termux/files/usr/bin/sh proot \ -0 \ --link2symlink \ -r ~/debian-stable \ -b /dev/ \ -b /sys/ \ -b /proc/ \ -b /data/data/com.termux/files/home \ /usr/bin/env \ -i \ HOME=/root \ TERM="xterm-256color" \ PATH=/bin:/usr/bin:/sbin:/usr/sbin \ /bin/bash --login

sh start.sh

wget -q https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux_10.sh | bash
