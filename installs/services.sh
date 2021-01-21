#!/data/data/com.termux/files/usr/bin/sh

echo -e "\ntermux-services Install\n"

echo -e "\ntermux-services contains a set of scripts for controlling services. Instead of putting commands in ~/.bashrc or ~/.bash_profile, they can be started and stopped with termux-services.\n"

echo -e "\nOnly a few packages so far contain the necessary service scripts, these are\n"

echo -e "\nmpd tor transmission sshd ftpd telnetd emacsd\n"

pkg install termux-services

echo -e "\nand then restart termux so that the service-daemon is started.\n"

echo -e "\nEnable and run a service\n"

sv-enable <service>

echo -e "\nIf you only want to run it once\n"

sv up <service>

echo -e "\nTo later stop a service, run\n"

echo -e "\nsv down <service>\n"

echo -e "\nOr to disable it\n"

echo -e "\nsv-disable <service>\n"

echo -e "\nA service is disabled if `$PREFIX/var/service/<service>/down` exists, so the `sv-enable` and `sv-disable` scripts touches, or removes, this file.\n"

echo -e "\ntermux-services uses the programs from runit to control the services. A bunch of example scripts are available from the same site. If you find a script you want to use, or if you write your own, you can use set it up by running\n"

mkdir -p $PREFIX/var/service/<PKG>/log

ln -sf $PREFIX/share/termux-services/svlogger $PREFIX/var/service/<PKG>/log/run

echo -e "and then put your run script for the package at $PREFIX/var/service/<PKG>/run and make sure that it is runnable.\n"

echo -e "\nYou can then run\n"

echo -e "\nsv up <PKG>\n"

echo -e "\nto start it.\n"

echo -e '\nLog files for services are situated in $PREFIX/var/log/sv/<PKG>/ with the active log file named "current".'

