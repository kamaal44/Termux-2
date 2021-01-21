#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nMOSH Install"

echo -e "\nMosh is a remote terminal application that allows roaming, supports intermittent connectivity, and provides intelligent local echo and line editing of user keystrokes."

echo -e "\nUsage example"

echo -e "\nImportant note: Mosh should be installed on both client and server side."

echo -e "\nConnecting to remote host (sshd listening on standard port):"

echo -e "\nmosh user@ssh.example.com"

echo -e "\nConnecting to Termux (sshd listening on port 8022):"

mosh --ssh="ssh -p 8022" 192.168.1.25
