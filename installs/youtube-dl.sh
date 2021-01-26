#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nInstall youtube-dl"

echo -e "\nDownload Youtube videos on your Android device by using Termux.it's very to install & download the youtube videos & audio From the Command Line with youtube-dl."

echo -e "\nStorage permission"

termux-setup-storage

echo -e "\ncURL"

pkg install -y curl

echo -e "\nInstall Python"

pkg install -y python

echo -e "\nffmpeg - For Audio Conversion"

pkg install -y ffmpeg

echo -e "\nInstall youtube-dl via cURL"

curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /data/data/com.termux/files/usr/bin/youtube-dl

echo -e "\nGive Permission to Execute the Script"

chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl

echo -e "\nVerify your Installation"

echo -e "\nwhich youtube-dl"

echo -e "\nLearn More about youtube-dl Command Line tool"

echo -e "\nyoutube-dl --help"

echo -e "\nUpdate Youtube-dl"

chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl youtube-dl -U

echo -e "\nDownload and Install via cURL Command"

curl -sL https://gist.githubusercontent.com/mskian/6ea9c2b32d5f41867e7cafc88d1b26d5/raw/youtube-dl.sh | bash

echo -e "\nUsage"

echo -e "\nYoutube Video and Audio Downloader for Android."

echo -e "\nyoutube-dl YOUTUBE VIDEO URL"

echo -e "\nList the Video Formats"

echo -e "\nyoutube-dl --list-formats YOUTUBEVIDEOURL"

echo -e "\nDownload youtube video by using Format code"

sleep 20

echo -e "\nyoutube-dl -f FORMATCODE YOUTUBEVIDEOURL"

echo -e "\nDownload as MP3"

echo -e "\nyoutube-dl --extract-audio --audio-format mp3 YOUTUBE VIDEO URL"

echo -e "\nUninstall youtube-dl from Termux"

echo -e "\nInstalled Location - /data/data/com.termux/files/usr/bin/"

echo -e "\nGoto youtube-dl installed location"

echo -e "\ncd /data/data/com.termux/files/usr/bin/"

echo -e "\nRemove/uninstall youtube-dl Software"

echo -e "\nrm youtube-dl"

sleep 20