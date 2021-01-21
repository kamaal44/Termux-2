#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nFish Install"

cd /sdcard/github/Termux/installs/

echo -e "\nFISH is a smart and user-friendly command line shell for macOS, Linux, and the rest of the family."

echo -e "\nThe FISH shell init files are ~/.fish, $PREFIX/etc/fish/config.fish and more."

echo -e "\nSee `man fish` and `info fish` for more information."

echo -e "\nOh-My-Fish of fish shell working without any known issue in termux, you can install it with official manual in the repository."

echo -e "\nFisherman is a fish-shell plugin manager."

curl -L https://get.oh-my.fish > install

fish install --offline=omf.tar.gz

echo -e "\nRun install --help for a complete list of install options you can customize."

echo -e "\nInstall a plugin. fisher z"

echo -e "\nInstall several plugins concurrently. fisher fzf edc/bass omf/thefuck omf/theme-bobthefish"

echo -e "\nInstall a specific branch. fisher edc/bass:master"

echo -e "\nInstall a specific tag. fisher edc/bass@1.2.0"

echo -e "\nInstall a gist. fisher https://gist.github.com/username/1f40e1c6e0551b2666b2"

echo -e "\nInstall a local plugin. fisher ~/path/to/my_plugin Edit your fishfile and run fisher to commit changes, e.g. install missing plugins. $EDITOR ~/.config/fish/fishfile fisher"

echo -e "\nShow everything you've installed. fisher ls @ my_plugin # a local plugin"

bobthefish # current theme

bass fzf thefuck z 

echo -e "\nShow everything available to install"

fisher ls-remote

echo -e "\nShow additional information about plugins:"

fisher ls-remote --format="%name(%stars): %info [%url]\n"

echo -e "\nUpdate everything."

fisher up

echo -e "\nUpdate specific plugins fisher up bass z fzf"

echo -e "\nRemove plugins. fisher rm thefuck"

echo Remove all the plugins. fisher ls | fisher rm

echo -e "\nOh My Fish Install"

cd /data/data/com.termux/files/home/

echo -e "\nInstall with Git"

git clone https://github.com/oh-my-fish/oh-my-fish

cd oh-my-fish

bin/install --offline # with a tarball
