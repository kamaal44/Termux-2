#!/data/data/com.termux/files/usr/bin/bash

# BuildAPKs

echo '\nReally quickly build APKs on handheld device (smartphone and tablet) in Amazon, Android, Chromebook, PRoot and Windows📲'

echo '\nhttps://buildapks.github.io/\n'

pkg install curl

cd ~

curl -O 'https://raw.githubusercontent.com/BuildAPKs/buildAPKs/master/setup.buildAPKs.bash'

wget 'https://raw.githubusercontent.com/BuildAPKs/buildAPKs.github/master/build.github.bash'

bash setup.buildAPKs.bash

bash build.github.bash

rm -rf setup.buildAPKs.bash build.github.bash
