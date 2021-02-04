#!/data/data/com.termux/files/usr/bin/sh

echo "\n"pyter Install"

echo "\n"pyter is a simple Translation Error Rate evaluation command."

cd /sdcard/github/Termux/python/

python3 -m pip install pyter

git clone git://github.com/aflc/pyter.git

cd pyter

python3 -m pip install -e .

python3 setup.py build

python3 setup.py install

rm -rf .git/ DOTgit .hgtags .hgignore

pyter --help > 'pyter help.txt'

pyter --help
