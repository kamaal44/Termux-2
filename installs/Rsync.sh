#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nRsync Install"

echo -e "\nRsync is a tool for synchronizing files with remote hosts or local directories (or drives). For better experience of using rsync, make sure that package `openssh` (or `dropbear`) is installed."

echo -e "\nUsage example"

echo -e "\nSync your photos with PC:"

rsync -av /sdcard/DCIM/ user@192.168.1.20:~/Pictures/Android/

echo -e "\nGet photos from remote Android device:"

rsync -av -e 'ssh -p 8022' 192.168.1.3:/sdcard/DCIM/ /sdcard/DCIM/

echo -e "\nSync local directories (e.g. from external sdcard to Termux home):"

rsync -av /storage/0123-4567/myfiles ~/files

echo -e "\nYou may want to see man page (`man rsync`) to learn more about it's usage."
