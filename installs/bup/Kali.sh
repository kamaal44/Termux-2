#!/data/data/com.termux/files/usr/bin/bash

echo "\n\e[93mThis script will install Kali Linux in Termux."

echo "\n\e[32m[*] \e[34mChecking for RootFS..."

folder="kali-fs"
if [ -d $folder ]; then
	first=1
	echo "\e[32m[*] \e[34mRootFS is already downloaded, skipping..."
fi
tarball="kali-rootfs.tar.gz"
if [ "$first" != 1 ];then
	if [ ! -f $tarball ]; then
		echo "\e[32m[*] \e[34mDetecting CPU architecture..."
		case `dpkg --print-architecture` in
		aarch64)
			archurl="arm64" ;;
		arm)
			archurl="armhf" ;;
		amd64)
			archurl="amd64" ;;
		x86_64)
			archurl="amd64" ;;	
		i*86)
			archurl="i386" ;;
		x86)
			archurl="i386" ;;
		*)
			echo; echo "\e[91mDetected unsupported CPU architecture!"; echo; exit ;;
		esac
		echo "\e[32m[*] \e[34mDownloading RootFS (~70Mb) for ${archurl}..."
		wget "https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Rootfs/Kali/${archurl}/kali-rootfs-${archurl}.tar.gz" -O $tarball -q
	fi
	cur=`pwd`
	mkdir -p "$folder"
	cd "$folder"
	echo "\n\e[32m[*] \e[34mDecompressing RootFS..."
	proot --link2symlink tar -xf ${cur}/${tarball}||:
	cd "$cur"
fi

mkdir -p kali-binds

bin="start-kali.sh"

echo "\n\e[32m[*] \e[34mCreating startup script..."

cat > $bin <<- EOM

#!/data/data/com.termux/files/usr/bin/bash

cd \$(dirname \$0)
## unset LD_PRELOAD in case termux-exec is installed
unset LD_PRELOAD
command="proot"
command+=" --link2symlink"
command+=" -0"
command+=" -r $folder"

if [ -n "\$(ls -A kali-binds)" ]; then
    for f in kali-binds/* ;do
      . \$f
    done
fi
command+=" -b /dev"
command+=" -b /proc"
command+=" -b kali-fs/tmp:/dev/shm"
## uncomment the following line to have access to the home directory of termux
#command+=" -b /data/data/com.termux/files/home:/root"
## uncomment the following line to mount /sdcard directly to / 
command+=" -b /sdcard"
command+=" -w /root"
command+=" /usr/bin/env -i"
command+=" HOME=/root"
command+=" PATH=/usr/local/sbin:/usr/local/bin:/bin:/usr/bin:/sbin:/usr/sbin:/usr/games:/usr/local/games"
command+=" TERM=\$TERM"
command+=" LANG=C.UTF-8"
command+=" /bin/bash --login"
com="\$@"
if [ -z "\$1" ];then
    exec \$command
else
    \$command -c "\$com"
fi
EOM

echo "\n\e[32m[*] \e[34mConfiguring Shebang..."

termux-fix-shebang $bin

echo "\n\e[32m[*] \e[34mSetting execution permissions..."

chmod +x $bin

echo "\n\e[32m[*] \e[34mRemoving RootFS image..."

rm -rf $tarball

echo "\n\e[32mKali Linux was successfully installed!\e[39m"

echo "\n\e[32mYou can now launch it by executing ./${bin} command.\e[39m"
