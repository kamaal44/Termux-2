#!/data/data/com.termux/files/usr/bin/sh

echo "\nInstall youtube-dl"

echo "\nDownload Youtube videos on your Android device by using Termux.it's very to install & download the youtube videos & audio From the Command Line with youtube-dl."

echo "\nStorage permission"

termux-setup-storage

echo "\ncURL"

pkg install -y curl

echo "\nInstall Python"

pkg install -y python

echo "\nffmpeg - For Audio Conversion"

pkg install -y ffmpeg

echo "\nInstall youtube-dl via cURL"

curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /data/data/com.termux/files/usr/bin/youtube-dl

echo "\nGive Permission to Execute the Script"

chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl

echo "\nVerify your Installation"

echo "\nwhich youtube-dl"

echo "\nLearn More about youtube-dl Command Line tool"

echo "\nyoutube-dl --help"

echo "\nUpdate Youtube-dl"

chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl youtube-dl -U

echo "\nDownload and Install via cURL Command"

curl -sL https://gist.githubusercontent.com/mskian/6ea9c2b32d5f41867e7cafc88d1b26d5/raw/youtube-dl.sh | bash

echo "\nUsage"

echo "\nYoutube Video and Audio Downloader for Android."

echo "\nyoutube-dl YOUTUBE VIDEO URL"

echo "\nList the Video Formats"

echo "\nyoutube-dl --list-formats YOUTUBEVIDEOURL"

echo "\nDownload youtube video by using Format code"

sleep 20

echo "\nyoutube-dl -f FORMATCODE YOUTUBEVIDEOURL"

echo "\nDownload as MP3"

echo "\nyoutube-dl --extract-audio --audio-format mp3 YOUTUBE VIDEO URL"

echo "\nUninstall youtube-dl from Termux"

echo "\nInstalled Location - /data/data/com.termux/files/usr/bin/"

echo "\nGoto youtube-dl installed location"

echo "\ncd /data/data/com.termux/files/usr/bin/"

echo "\nRemove/uninstall youtube-dl Software"

echo "\nrm youtube-dl"

sleep 20