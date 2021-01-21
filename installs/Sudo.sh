#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nTermux Sudo Install"

cd /data/data/com.termux/files/home/

git clone https://gitlab.com/st42/termux-sudo

cat termux-sudo/sudo > /data/data/com.termux/files/usr/bin/sudo

chmod 700 /data/data/com.termux/files/usr/bin/sudo

cd ..

rm -rf termux-sudo/

clear

echo -e "\nAndroid-Sudo v1.1 Install"

echo -e "\n-------------------------"

if [ "`id | grep =0`" ]; then
    echo -e "\n[sudo] Installing sudo..."
    printf "[sudo] Enter new password for root (leave empty for none): "
    read pass
    if [ "$pass" == "" ]; then
        nopswd=1
    else
        printf "[sudo] Confirm password: "
        read passconf
        if [ "$pass" == "$passconf" ]; then
            nopswd=0
        else
            echo -e "\n[sudo] Passwords do not match, exiting..."
            exit 1
        fi
    fi
    echo -e "\n[sudo] Remounting system as rw..."
    mount -o rw,remount /system > /dev/null 2>&1
    if [ "$?" == "0" ]; then
        if [ "$nopswd" == "0" ]; then
            echo -e "\n[sudo] Creating configuration file..."
            echo -e "\n$pass" > /etc/sudo.conf
            chmod 0600 /etc/sudo.conf
            echo -e "\n[sudo] Creating wrapper script..."
            echo -e "\n#!/system/bin/sh

cmd=\"\$@\"
su -c \"mount -o rw,remount /system > /dev/null 2>&1\"
su -c \"chmod 0644 /etc/sudo.conf\"
rootpass=\"\$(cat /etc/sudo.conf)\"
su -c \"chmod 0600 /etc/sudo.conf\"
su -c \"mount -o ro,remount /system > /dev/null 2>&1\"
printf \"[sudo] Enter password for root: \"
read inputpass
if [ \"\$inputpass\" == \"\$rootpass\" ]; then
    su -c \"\$cmd\"
else
    echo \"[sudo] Authentication failed!\"
    exit 1
fi" > /system/bin/sudo
        else
            echo -e "\n[sudo] Creating wrapper script..."
            echo -e "\n#!/system/bin/sh

cmd=\"\$@\"
su -c \"\$cmd\"" > /system/bin/sudo
        fi
        chmod 0755 /system/bin/sudo
        echo -e "\n[sudo] Remounting system as ro..."
        mount -o ro,remount /system > /dev/null 2>&1
        if [ "$?" == "0" ]; then
            :
        else
            echo -e "\n[sudo] Mounting failed, ignoring..."
        fi
        echo -e "\n[sudo] Installation finished!"
    else
        echo -e "\n[sudo] Mounting failed, exiting..."
        exit 1
    fi
else
    echo -e "\n[sudo] Installer should be ran as root, exiting..."
    exit 1
fi

