#!/system/bin/sh

echo -e "\nZip Install"

echo -e "\nFisrt update and install requirments .."

apt update -y

apt upgrade -y

apt install -y zip

apt install -y unzip
