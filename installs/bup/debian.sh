#!/data/data/com.termux/files/usr/bin/sh

echo "\nDebian on Termux"

echo "\nsome configuration. adapt this to your needs"

cd /data/data/com.termux/files/home/

DO_FIRST_STAGE=:  #false   # required (unpack phase/ executes outside guest invironment)
DO_SECOND_STAGE=: #false   # required (complete the install/ executes inside guest invironment)
DO_THIRD_STAGE=:  #false   # optional (enable local policies/ executes inside guest invironment)
VERSION=stable             # debian versions: stable, testing, unstable
ROOTFS_TOP=deboot_debian   # name of the top install directory

echo "\nsome automatic configuration"

set -e
trap '[ $? -eq 0 ] && exit 0 || (echo; echo "\ntermux-info:"; termux-info)' EXIT
ZONEINFO=$(getprop persist.sys.timezone)     # set your desired time zone
ARCHITECTURE=$(uname -m)
case $ARCHITECTURE in    # supported architectures include: armel, armhf, arm64, i386, amd64
    aarch64) ARCHITECTURE=arm64 ;;
    x86_64) ARCHITECTURE=amd64 ;;
    armv7l) ARCHITECTURE=armhf ;;
    armv8l) ARCHITECTURE=armhf ;;
    armel|armhf|arm64|i386|amd64|mips|mips64el|mipsel|ppc64el|s390x) ;;
    # Officially supported Debian Stretch architectures
    *) echo "\nUnsupported architecture $ARCHITECTURE"; exit ;;
esac

patchme() {

echo "\nminimum patch needed for debootstrap to work in this environment"

patch -l << 'EOF' 
--- functions.a 2020-02-27 13:16:24.000000000 +0100
+++ functions   2020-03-03 11:24:15.810995745 +0100
@@ -1154,6 +1154,10 @@
 }
 
 setup_proc () {
+
+echo skipping setup_proc
+return 0
+
        case "$HOST_OS" in
            *freebsd*)
                umount_on_exit /dev
@@ -1265,6 +1269,10 @@
 
 
 setup_devices_simple () {
+
+echo skipping setup_devices_simple
+return 0
+
        # The list of devices that can be created in a container comes from
        # src/core/cgroup.c in the systemd source tree.
        mknod_if_needed "$TARGET/dev/null"        c 1 3
@@ -1589,6 +1597,11 @@
 # this directory. (Both may be forbidden by mount options, e.g. nodev and
 # noexec respectively.)
 check_sane_mount () {
+
+# these checks make no sense in our environment and fail anyway -> skip
+echo skipping check_sane_mount
+return 0
+
        mkdir -p "$1"
 
        case "$HOST_OS" in
EOF
    return $?
}

USER_ID=$(id -u)
USER_NAME=$(id -un)
unset LD_PRELOAD # just in case termux-exec is installed

echo "\nworkaround https://github.com/termux/termux-app/issues/306"
echo "\nworkaround https://github.com/termux/termux-packages/issues/1644"
echo "\nor expect 'patch' to fail when doin the install via ssh and sh (not bash) is used"

export TMPDIR=$PREFIX/tmp
cd

echo "\nfirst stage - do the initial unpack phase of bootstrapping only"

$DO_FIRST_STAGE && {
echo ======== DO_FIRST_STAGE ========

[ -e "/data/data/com.termux/files/home/$ROOTFS_TOP" ] && {
    echo the target install directory already exists, to continue please remove it by
    echo rm -rf "/data/data/com.termux/files/home/$ROOTFS_TOP"
    exit
}
apt-get -qq update

unset RESOLV
[ -e "$PREFIX/etc/resolv.conf" ] || {
    RESOLV=resolv-conf
}

DEBIAN_FRONTEND=noninteractive apt-get -yqq install coreutils perl proot sed wget gnupg $RESOLV
hash -r

echo "\nfirst try to patch the most recent original of debian debootstrap script"
rm -rf debootstrap
V=$(wget http://http.debian.net/debian/pool/main/d/debootstrap/ -qO - \
    | sed 's/<[^>]*>//g' \
    | grep -E '\.[0-9]+\.tar\.gz' \
    | tail -n 1 \
    | sed 's/^ +//g;s/.tar.gz.*//g')
wget "http://http.debian.net/debian/pool/main/d/debootstrap/$V.tar.gz" -qO - | tar xfz -
V=$(echo "\n$V" | sed 's/_/-/g')
ln -nfs "$V" debootstrap
cd debootstrap

patchme || {
# echo "\nif the above fails patch the last known good backup of an older version of debian debootstrap script"
cd
echo "\npatching $V failed using fallback"
rm -rf debootstrap
V=debootstrap_1.0.119
wget "https://github.com/sp4rkie/debian-on-termux/blob/master/$V.tgz?raw=true" -qO - \
        | tar xfz -
V=$(echo "\n$V" | sed 's/_/-/g')
ln -nfs "$V" debootstrap
cd debootstrap
patchme
}

echo "\nfix https://github.com/sp4rkie/debian-on-termux/issues/21"
echo "\nfix https://github.com/sp4rkie/debian-on-termux/issues/63"

echo "\nadd the key for stable (Debian Stable Release Key)"
apt-key adv --recv-keys DCC9EFBF77E11517
echo "\nadd the keys for testing, unstable (Debian Archive Automatic Signing Key)"
apt-key adv --recv-keys 648ACFD622F3D138

echo "\nyou can watch the debootstrap progress via tail -F /data/data/com.termux/files/home/$ROOTFS_TOP/debootstrap/debootstrap.log"

DEBOOTSTRAP_DIR="$(pwd)"
export DEBOOTSTRAP_DIR
O="$("$PREFIX/bin/proot" \
    -b /system \
    -b /vendor \
    -b /data \
    -b "$PREFIX/bin:/bin" \
    -b "$PREFIX/etc:/etc" \
    -b "$PREFIX/lib:/lib" \
    -b "$PREFIX/share:/share" \
    -b "$PREFIX/tmp:/tmp" \
    -b "$PREFIX/var:/var" \
    -b /dev \
    -b /proc \
    -r "$PREFIX/.." \
    -0 \
    --link2symlink \
    ./debootstrap --keyring="$PREFIX/etc/apt/trusted.gpg" \
        --foreign --arch="$ARCHITECTURE" "$VERSION" "/data/data/com.termux/files/home/$ROOTFS_TOP" 2>&1 || true)"
echo "\n$O" > ~/debian-on-termux_debootstrap.log
echo "\nproot returns invalid exit status"
if echo "\n$O" | grep " error: " > /dev/null ; then
    echo "\n$O"
    exit 1
fi
} # end DO_FIRST_STAGE

echo "\nsecond stage - complete the bootstrapping process"

$DO_SECOND_STAGE && {
echo ======== DO_SECOND_STAGE ========

echo "\nsince there are issues with proot and /proc mounts (https://github.com/termux/termux-packages/issues/1679)"
echo "\nwe currently cease from mounting /proc."
echo "\nthe guest system now is setup to complete the installation - just dive in"
echo "\nUPDATE as of 2017_11_27:"
echo "\nissue https://github.com/termux/termux-packages/issues/1679#ref-commit-bcc972c now got fixed."
echo "\n/proc now included in mount list"

O="$("$PREFIX/bin/proot" \
    -b /dev \
    -b /proc \
    -r "/data/data/com.termux/files/home/$ROOTFS_TOP" \
    -w /root \
    -0 \
    --link2symlink /usr/bin/env \
    -i HOME=/root TERM=xterm /debootstrap/debootstrap --second-stage 2>&1 || true)"
echo "\n$O" > ~/debian-on-termux_debootstrap_stage2.log
echo "\nproot returns invalid exit status"
if echo "\n$O" | grep " error: " > /dev/null ; then
    echo "\n$O"
    exit 1
fi

echo "\nAdd termux user in the passwd, group and shadow."

echo "\n$USER_NAME:x:$USER_ID:$USER_ID::/home/$USER_NAME:/bin/bash" >> \
    "/data/data/com.termux/files/home/$ROOTFS_TOP/etc/passwd"
echo "\n$USER_NAME:x:$USER_ID:" >> \
    "/data/data/com.termux/files/home/$ROOTFS_TOP/etc/group"
echo "\n$USER_NAME:*:15277:0:99999:7:::" >> \
    "/data/data/com.termux/files/home/$ROOTFS_TOP/etc/shadow"

echo "\nadd the termux user homedir to the new debian guest system"

mkdir -p "/data/data/com.termux/files/home/$ROOTFS_TOP/home/$USER_NAME"
chmod 755 "/data/data/com.termux/files/home/$ROOTFS_TOP/home/$USER_NAME"
} # end DO_SECOND_STAGE

echo "\noptional third stage - if enabled edit some system defaults - adapt this to your needs"

$DO_THIRD_STAGE && {
echo ======== DO_THIRD_STAGE ========

echo "\ntake over an existing 'resolv.conf' from the host system (if there is one)"

[ -e "/data/data/com.termux/files/home/$ROOTFS_TOP/etc/resolv.conf" ] || {
    cp "$PREFIX/etc/resolv.conf" "/data/data/com.termux/files/home/$ROOTFS_TOP/etc/resolv.conf"
    chmod 644 "/data/data/com.termux/files/home/$ROOTFS_TOP/etc/resolv.conf"
}

echo "\nto enter the debian guest system execute '/data/data/com.termux/files/home/bin/enter_deb' on the termux host system"

mkdir -p "/data/data/com.termux/files/home/bin"
cat << EOF > "/data/data/com.termux/files/home/bin/enter_deb"

#!/data/data/com.termux/files/usr/bin/sh

unset LD_PRELOAD
SHELL_=/bin/bash
ROOTFS_TOP_=$ROOTFS_TOP
ROOT_=1
USER_=$USER_NAME
EOF
cat << 'EOF' >> "/data/data/com.termux/files/home/bin/enter_deb"

SCRIPTNAME=enter_deb
show_usage () {
    echo "\nUsage: $SCRIPTNAME [options] [command]"
    echo "\n$SCRIPTNAME: enter the installed debian guest system"
    echo "\n"
    echo "\n  -0 - mimic root (default)"
    echo "\n  -n - prefer regular termux uid ($USER_)"
    exit 0
}

while getopts :h0n option
do
    case "$option" in
        h) show_usage;;
        0) ;;
        n) ROOT_=0;;
        ?) echo "\n$SCRIPTNAME: illegal option -$OPTARG"; exit 1;
    esac
done
shift $(($OPTIND-1))

HOMEDIR_=/home/$USER_
[ $ROOT_ = 1 ] && {
    CAPS_=$CAPS_"-0 "
    HOMEDIR_=/root
}
CMD_="$SHELL_ -l"
[ -z "$*" ] || {
    CMD_='sh -c "$*"'
}
eval $PREFIX/bin/proot \
    -b /dev \
    -b /proc \
    -r /data/data/com.termux/files/home/$ROOTFS_TOP_ \
    -w $HOMEDIR_ \
    $CAPS_ \
    --link2symlink \
    /usr/bin/env -i HOME=$HOMEDIR_ TERM=$TERM LANG=$LANG $CMD_
EOF
chmod 755 "/data/data/com.termux/files/home/bin/enter_deb"

cat << 'EOF' > "/data/data/com.termux/files/home/$ROOTFS_TOP/root/.profile"
# ~/.profile: executed by Bourne-compatible login shells.

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi
EOF

cat << EOF > "/data/data/com.termux/files/home/$ROOTFS_TOP/tmp/dot_tmp.sh"
#!/bin/sh

filter() {
    egrep -v '^$|^WARNING: apt does'
}

# select 'vi' as default editor for debconf/frontend

update-alternatives --config editor << !
2
!

# prefer a text editor for debconf (a GUI makes no sense here)

cat << ! | debconf-set-selections -v
debconf debconf/frontend                       select Editor
debconf debconf/priority                       select low
locales locales/locales_to_be_generated        select en_US.UTF-8 UTF-8
locales locales/default_environment_locale     select en_US.UTF-8
!
ln -nfs /usr/share/zoneinfo/$ZONEINFO /etc/localtime
dpkg-reconfigure -fnoninteractive tzdata
dpkg-reconfigure -fnoninteractive debconf

DEBIAN_FRONTEND=noninteractive apt -y update 2>&1 | filter                    
DEBIAN_FRONTEND=noninteractive apt -y upgrade 2>&1 | filter
DEBIAN_FRONTEND=noninteractive apt -y install locales 2>&1 | filter
update-locale LANG=en_US.UTF-8 LC_COLLATE=C

# place any additional packages here as you like

#DEBIAN_FRONTEND=noninteractive apt -y install rsync less gawk ssh 2>&1 | filter  
apt clean 2>&1 | filter
EOF
chmod 755 "/data/data/com.termux/files/home/$ROOTFS_TOP/tmp/dot_tmp.sh"

"$PREFIX/bin/proot" \
    -b /dev \
    -b /proc \
    -r "/data/data/com.termux/files/home/$ROOTFS_TOP" \
    -w /root \
    -0 \
    --link2symlink \
    /usr/bin/env -i HOME=/root TERM=xterm PATH=/usr/sbin:/usr/bin:/sbin:/bin /tmp/dot_tmp.sh \
        || : # proot returns invalid exit status
echo 
echo installation successfully completed
echo to enter the guest system type:
echo "\n\/data/data/com.termux/files/home/bin/enter_deb"
echo

} # end DO_THIRD_STAGE
