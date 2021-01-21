#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nRuby Install"

pkg install ruby

echo -e "\nListing installed gems"

gem list --local

echo -e "\nLaunching a local documentation and gem repository server"

gem server

echo -e "\nWhen installing Ruby gems, it is highly recommended to have a package build-essential to be installed - some gems compile native extensions during their installation."
