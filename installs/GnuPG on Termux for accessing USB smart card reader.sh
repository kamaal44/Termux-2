pkg install libusb-dev apt autoconf automake bash binutils busybox ca-certificates clang command-not-found coreutils darkhttpd dash diffutils dirmngr dpkg emacs findutils gawk gdbm gettext git glib gnupg gnutls golang gpgv grep hunspell hunspell-en-us ldns less libandroid-glob libandroid-support libandroid-support-dev libassuan libassuan-dev libbz2 libc++ libcroco libcrypt libcrypt-dev libcurl libedit libffi libgcrypt libgcrypt-dev libgmp libgnutls libgnutls-dev libgpg-error libgpg-error-dev libidn libidn2 libidn2-dev libksba libksba-dev libllvm libltdl liblzma libmpfr libnettle libnettle-dev libnghttp2 libnpth libnpth-dev libsqlite libtalloc libtool libunistring libusb libusb-dev libutil libxml2 lynx m4 make man ncurses ncurses-ui-libs ndk-stl ndk-sysroot openssh openssl pcre pcre2 perl pinentry proot python python-dev readline readline-dev resolv-conf screen sed termux-am termux-api termux-exec termux-tools texinfo tsu vim vim-runtime
cd $HOME
mkdir -p src
cd src
git clone git://git.gnupg.org/gnupg.git
cd gnupg
git checkout gnupg-2.2.12 # matches GnuPG in Termux
export C_INCLUDE_PATH="$PREFIX/include/:$PREFIX/include/libusb-1.0/:$PREFIX/include/libandroid-support"
./autogen.sh
./configure --enable-maintainer-mode --disable-doc --with-pinentry-pgm="$PREFIX/bin/pinentry-curses" --with-scdaemon-pgm="$PWD/scd/scdaemon" --host=aarch64-unknown-linux-android
make -j 4
./build–aux/config.guess
aarch64-unknown-linux-gnu
tsu
gpgconf --kill all
"$HOME/src/gnupg/agent/gpg-agent" --homedir "$HOME/.gnupg/" --daemon
chown -R u0_a88.u0_a88 ~/.gnupg
gpg --card-status
