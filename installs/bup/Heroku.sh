#!/data/data/com.termux/files/usr/bin/sh

echo "\nHeroku Install"

cd /data/data/com.termux/files/home/

pkg install -y wget

pkg install -y nano

pkg install -y tar

pkg install -y gzip

pkg install -y nodejs

wget http://cli-assets.heroku.com/heroku-linux-arm.tar.gz -O heroku.tar.gz

tar -xvzf heroku.tar.gz

rm -rf heroku.tar.gz

mkdir -p /data/data/com.termux/files/usr/lib/

cp -R heroku/ /data/data/com.termux/files/usr/lib/

rm -rf heroku

ln -s /data/data/com.termux/files/usr/lib/heroku/bin/heroku /data/data/com.termux/files/usr/bin/heroku

echo "\nHeroku will not work as its script is pointing to /usr/bin/env whereas our path on Termux differs."

echo "\nTo direct Heroku to the right path, first install nano (or your own favourite editor), then edit Heroku’s script:"

cd /data/data/com.termux/files/usr/lib/heroku/bin/

#!/data/data/com.termux/files/usr/bin/bash

echo "\nChange this line to:"

echo "\nNow Heroku is not yet working, one more fix and we’ll be done."

echo "\nThe tarball file does contain a necessary node.js binary but it does not work in Termux. you will have to install it with the Linux environment and point Heroku to its path."

touch heroku
sleep 20s

nano heroku

cd /data/data/com.termux/files/usr/lib/heroku/bin

mv node node.old

ln -s ../../../bin/node node

echo "\nWhen asked, press any key (expect ‘q’) to open a web browser and login your Heroku account."

echo "\nDone"
