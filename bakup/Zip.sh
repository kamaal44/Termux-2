#!/system/bin/sh

echo "\nZip Install"

echo "\nFisrt update and install requirments .."

apt update -y

apt upgrade -y

apt install -y zip

apt install -y unzip
