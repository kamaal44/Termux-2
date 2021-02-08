#!/data/data/com.termux/files/usr/bin/sh

echo "\nMOSH Install"

echo "\nMosh is a remote terminal application that allows roaming, supports intermittent connectivity, and provides intelligent local echo and line editing of user keystrokes."

echo "\nUsage example"

echo "\nImportant note: Mosh should be installed on both client and server side."

echo "\nConnecting to remote host (sshd listening on standard port):"

echo "\nmosh user@ssh.example.com"

echo "\nConnecting to Termux (sshd listening on port 8022):"

mosh --ssh="ssh -p 8022" 192.168.1.25
