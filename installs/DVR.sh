#!/data/data/com.termux/files/usr/bin/sh

echo -e "\DVR Install"

echo -e "\nTermux is a DVR (Digital Video Recorder) in the palm of my hand, as well as in my pocket."

pkg install -y python

python3 -m pip install youtube-dl

pkg install play-audio

echo -e "\nThis will play your favorite song forever. Use ctrl+c to exit this eternal trance loop."

echo -e "\nwhile true; do play-audio favoriteSong.file; done"
