#!/data/data/com.termux/files/usr/bin/sh

echo "\n####  <-- Moving To Home -->  ####"
cd /data/data/com.termux/files/home
echo "\n####  <-- Creating home.zip -->  ####\n"
zip home.zip -9 -r .* *
echo "\n####  <-- Moving home.zip -->  ####\n"
mv -v -f /data/data/com.termux/files/home/home.zip /sdcard/github/Termux/home/
cd /sdcard/github/Termux/home/
echo "\n####  <-- Unzipping home.zip -->  ####\n"
unzip -o home.zip
echo "\n####  <-- Removing home.zip -->  ####\n"
rm -rf /sdcard/github/Termux/home/home.zip
echo "####  <-- DONE -->  ####\n"
