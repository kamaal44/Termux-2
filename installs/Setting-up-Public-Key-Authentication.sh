#!/system/bin/sh

# Setting up Public Key Authentication

echo -e "\nSetting up public key authentication"

echo -e "\nPublic key authentication is the recommended way for logging in using SSH. To use this type of authentication, you need to have a public/private key pair. For successful login, the public key must exist in the authorized keys list on remote machine while private key should be kept safe on your local host."

echo -e "\nIn the following example it will be assumed that you want to establish public key authentication between your PC (host) and your Android device running Termux (remote). It also will be assumed that you running Linux distribution on your PC."

echo -e "\n1. If you do not have keys, you can generate them. In this example we will generate RSA key. On PC, execute this command:"

ssh-keygen -t rsa -b 2048 -f id_rsa

echo -e "\nThe command shown above generates private RSA key with 2048 bit key length and saves it to file `id_rsa`. In the same directory you can find a file `id_rsa.pub` – it is a public key."

echo -e "\nImportant note: 2048 bit is the minimal key length that is considered safe. You can use higher values, but do not use higher than 4096 as remote server may not support big keys."

echo -e "\n2. Copy key to the remote machine (Termux). Password authentication has to be enabled in order to install pubkey on remote machine. Now do:"

ssh-copy-id -p 8022 -i id_rsa IP_ADDRESS

echo -e "\nDo not forget to replace `IP_ADDRESS` with the actual LAN IP address of your device. It can be determined by using command ifconfig."

echo -e "\nNow try logging into the machine, with:   "ssh -p '8022' '192.168.1.4'"

ssh -p '8022' '192.168.1.4'

echo -e "\nand check to make sure that only the key(s) you wanted were added."

echo -e "\n3. From this point password authentication can be disabled. Edit file $PREFIX/etc/ssh/sshd_config and replace line beginning with 'PasswordAuthentication' by"
sleep 10

nano -Lc $PREFIX/etc/ssh/sshd_config

PasswordAuthentication no

echo -e "\nThen execute command pkill sshd; sshd in order to restart server with updated configuration file."

pkill sshd
