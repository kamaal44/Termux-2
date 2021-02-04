#!/data/data/com.termux/files/usr/bin/sh

echo "\nRuby Install"

pkg install ruby

echo "\nListing installed gems"

gem list --local

echo "\nLaunching a local documentation and gem repository server"

gem server

echo "\nWhen installing Ruby gems, it is highly recommended to have a package build-essential to be installed - some gems compile native extensions during their installation."
