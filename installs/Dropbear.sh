#!/data/data/com.termux/files/usr/bin/sh

# Dropbear Install

echo "\nDropbear Install"

cd /sdcard/github/Termux/apps/

echo "\nMake sure that everything is up to date and dropbear is installed:"

apt update -y && apt upgrade -y

pkg update -y && pkg upgrade -y

pkg install -y dropbear

echo "\nSet password by executing command passwd."

passwd

echo "\nStart dropbear server. You can execute either just dropbear to start it in background or dropbear -F to start it in the foreground."

echo "\nDropbear does not provide SFTP server."

echo "\nStarting and stopping Dropbear server"

echo "\nSame as for OpenSSH, you will need to execute it's binary manually. Also, unlike OpenSSH, Dropbear does not use a configuration file but only command line arguments."

echo "\nServer is running in background, both password and public key authentication available. To achieve this, just type in console:"

dropbear

echo "\nIf you need only public key authentication, do this instead:"

dropbear -s

echo "\nAlso, server can be started in foreground. For this purpose use a parameter `-F`:"

dropbear -F

echo "\nServer started in foreground can be stopped by just Ctrl-C key combination. If it is in the background, then you can use a `pkill`:"

echo "\npkill dropbear"
sleep 5

echo "\nSetting up password authentication"

echo "\nSame as for OpenSSH, password authentication is enabled by default."

echo "\nEverything you have to do, is:"

echo "\nSetting up public key authentication"

echo "\nSame as for OpenSSH, you can put your keys by using ssh-copy-id. But if you consider to setup a public key authentication from Termux to something else, it is worth to mention some important differences between OpenSSH and Dropbear."

echo "\n1. Dropbear uses a different command for generating keys. Example of generating RSA key (2048 bit):"

dropbearkey -t rsa -f id_rsa -s 2048

echo "\n2. Public key should be obtained manually. To do this, you have to use 'dropbearkey' again, but in different way:"

dropbearkey -f id_rsa -y

echo "\n3. Dropbear and OpenSSH uses a different key formats. To use a Dropbear's key in OpenSSH, you will have to convert it:"

dropbearconvert dropbear openssh ./id_rsa ./id_rsa_openssh

echo "\nThis procedure can be done vice versa to obtain a key in Dropbear's format:"

dropbearconvert openssh dropbear ./id_rsa_openssh ./id_rsa_dropbear

echo "\nUsing the SFTP"

echo "\nPackage OpenSSH provides a tool for accessing remote hosts over SFTP. This will allow you to work with files in same way as via FTP but with better security.

echo "\nConnecting to Termux (sshd listening on port 8022):"

echo sftp -P 8022 192.168.1.20

echo "\nConnecting to somewhere else (sshd listening on standard port):"

echo sftp sftp.example.com

echo "\nHowever, to use command line SFTP client you should know some basic commands:"

mkdir PATH

echo "\nmkdir PATH - create directory `PATH`."

echo "\ncd PATH - change current directory to `PATH`.

cd PATH

echo "\nget REMOTE [LOCAL] - download file `REMOTE` and rename it as `LOCAL` (optional)."

echo "\nls [PATH] - list files in directory `PATH`. If no argument, files in current directory will be listed."

echo "\nput LOCAL [REMOTE] - Upload file `LOCAL` and rename it as `REMOTE` (optional)."

echo "\nrm FILE - Delete file `FILE`."

echo "\nThis is not a complete list of SFTP commands. To view all available commands, consider to view man page (man sftp) or view short help in interactive SFTP session by issuing command `help`."
