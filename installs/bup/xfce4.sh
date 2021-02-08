#!/data/data/com.termux/files/usr/bin/sh

echo "\nxfce4 Install"

echo "\nGet the necessary components"

apt-get update -y

apt-get install -y xfce4

apt-get install -y xfce4-terminal

apt-get install -y tightvncserver

apt-get install -y xfe

apt-get clean

echo "\nSetup the necessary files"

mkdir -p /data/data/com.termux/files/home/.vnc

wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/xstartup -P /data/data/com.termux/files/home/.vnc/

wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/vncserver-start -P /usr/local/bin/

wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/vncserver-stop -P /usr/local/bin/

chmod +x /data/data/com.termux/files/home/.vnc/xstartup

chmod +x /usr/local/bin/vncserver-start

chmod +x /usr/local/bin/vncserver-stop

echo "\nYou can now start vncserver by running vncserver-start"

echo "\nIt will ask you to enter a password when first time starting it."

echo "\nThe VNC Server will be started at 127.0.0.1:5901"

echo "\nYou can connect to this address with a VNC Viewer you prefer"

echo "\nConnect to this address will open a window with Xfce4 Desktop Environment"

echo "\nRunning vncserver-start"

echo "\nTo Kill VNC Server just run vncserver-stop"

echo "\nexport DISPLAY=":1"" >> /etc/profile

source /etc/profile

vncserver-start
