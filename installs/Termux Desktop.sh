# Termux Desktop

echo "Termux Desktop Install"

pkg update -y
pkg upgrade -y
apt update -y
apt upgrade -y'
pip install upgrade pip
npm install -g npm
cd $HOME
git clone --depth=1 https://github.com/adi1090x/termux-desktop.git
cd termux-desktop/
chmod +x setup.sh
./setup.sh --install
echo "\nTo start run: startdesktop\n"
startdesktop
