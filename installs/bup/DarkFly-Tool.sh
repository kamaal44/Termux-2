#!/data/data/com.termux/files/usr/bin/sh

echo "\nInstall DarkFly-Tool"

echo "\nThe advantage of installing this tool is that you don't have to search for a tool manually every time you wanna perform a different type of attack you can just use darkfly tool to suggest you the tools that are suitable for you."

echo "\nTo install any tool from Github in Termux we have to install the git package in termux we are also installing the python2 package because this tool runs on python2. Use the below command to install python and git package in termux."

pkg install -y python git

echo "\nNow we have to clone the project from the git hub repository using the git clone command."

cd /sdcard/github/Termux/python/

git clone https://github.com/Ranginang67/DarkFly-Tool.git

echo "\nChange the directory to the DarkFly folder if you don't know the cd command its highly recommended to check out this blog:[termux all basic command]."

cd DarkFly-Tool

echo "\nNow the DarkFly project is downloaded in your Termux app, you just have to run the install.py file to install The project on your system."

python3 install.py

echo "\nNow Installation is completed. Use DarkFly-Tool in Termux:"

echo "\nPlease Restart Termux Before Following these steps."

echo "\nNow You can type DarkFly to run the tool anytime you want"

echo "\nStep 2: Now you will see 5 options you can select any option but the main option is the 1st one. you can also use spam tools by typing 2 but I am selecting the 1st option."

echo "\nType 1 and press ENTER."

echo "\nNow you will see a list of 530 tools that are specially made for termux, Select any tool by typing its serial number and the tool will be Downloaded in your Termux."
