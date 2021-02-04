#!/data/data/com.termux/files/usr/bin/sh

echo "\nTermux + QEMU + Alpine Linux = Docker on Stock ChromeOS"

echo "\nNo Developer Mode Needed"

cd /sdcard/github/Termux/apps/

git clone https://github.com/termux/termux-app.git

git clone https://github.com/xeffyr/termux-x-repository.git

pkg update -y && pkg upgrade -y

pkg install -y coreutils

pkg install -y termux-tools

pkg install -y proot

pkg install -y util-linux

pkg install -y net-tools

pkg install -y openssh

pkg install -y git

pkg install -y wget

termux-setup-storage

wget https://raw.githubusercontent.com/xeffyr/termux-x-repository/master/enablerepo.sh | bash

pkg install -y qemu-system

git clone https://github.com/pwdonald/chromeos-qemu-docker.git

echo "\nCreate Virtual Storage Device: (NOTE: make sure you're aware of what directory you're in i.e. /storage/emulated/0/Download can be wiped by ChromeOS periodically as space is needed so backup often!)"

sleep 5s

qemu-img create -f qcow2 virtual_drive 4G

wget -O alpine_x86_64.iso http://www.example.com/ http://dl-cdn.alpinelinux.org/alpine/latest-stable/main/x86_64/

sh ./chromeos-qemu-docker/scripts/setup_alpine.sh

echo "\nThis script should be run in whichever directory your virtual drive exists to start the VM."

sleep 5s

echo "\nThis may take a few minutes to start, resulting in a black screen with a cursor."

sleep 5s

echo "\nIf you've been using the Termux session for a while you may see some of your history creep into view instead of a black screen."

sleep 5s

echo "\nOnce inside the VM:"

sleep 5s

echo "\nLogin with username root."

sleep 5s

setup-alpine

echo "nameserver 8.8.8.8 > /etc/resolv.conf"

sleep 5s

alpine-setup

echo "\nOnce the `alpine-setup` script is complete--it will instruct you to restart the machine.

sleep 5s

echo "\nTo exit the VM Press **Ctrl + A, X**."

sleep 5s

echo "\nCongrats! You've installed Alpine Linux!**"

sleep 5s

sh ./chromeos-qemu-docker/scripts/start_persist.sh

echo "\nLogin with root & the password you setup

sleep 5s

echo "\nYou may have to add your nameservers again.

sleep 5s

apk --no-cache update

apk --no-cache add nano

apk --no-cache add docker

echo "\nDocker is now installed!**

echo "\nStart the docker service with

sleep 5s

service docker start

echo "\nYou can now use docker as you would in a traditional environment.

sleep 5s

echo "\nThe `start_persist.sh` script maps ports 22 and 80 from the virtual environment to 10022 and 10080 respectively on the Termux environment. You can utilize these ports from your ChromeOS env by finding the IP address of your Termux session.

sleep 5s
