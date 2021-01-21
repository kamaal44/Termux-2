#!/data/data/com.termux/files/usr/bin/sh

echo "FZF Install"

cd /data/data/com.termux/files/home/

git clone --depth 1 https://github.com/junegunn/fzf.git /data/data/com.termux/files/home/.fzf

cd .fzf

rm -rf .git/ .github/ .gitignore  CHANGELOG.md LICENSE Dockerfile

sh install
