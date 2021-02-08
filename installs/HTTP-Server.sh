#!/data/data/com.termux/files/usr/bin/sh

echo "\nSetting up HTTP Server"

pkg install -y autoconf

pkg install -y automake

pkg install -y bison bzip2

pkg install -y clang

pkg install -y cmake

pkg install -y coreutils

pkg install -y diffutils

pkg install -y flex

pkg install -y gawk

pkg install -y git

pkg install -y grep

pkg install -y gzip

pkg install -y libtool

pkg install -y make

pkg install -y patch

pkg install -y perl

pkg install -y sed

pkg install -y silversearcher-ag

pkg install -y tar

pkg install -y apache2

pkg install -y php

pkg install -y php-apache

echo "\nInstalling and configuring apache2"

echo "\nIn this and further steps you will need to acces the `/etc` folder, but in termux it is hidden in `/data/data/com.termux/files/usr/etc/`, so I suggest you to make link."

ln -s /data/data/com.termux/files/usr/etc/ /data/data/com.termux/files/home/etc

echo "\nYou can configure it if you need in `/data/data/com.termux/files/home/etc/apache2/httpd.conf`."

echo "\nNow you can run apache2 server by simple `httpd` (by default it will run on 127.0.0.1:8080)."

echo "\nAccording to archwiki page `libphp7.so` included with `php-apache` will only work with `mod_mpm_prefork`."

echo "\n* In `/data/data/com.termux/files/home/etc/apache2/httpd.conf` comment following line:"

echo "\nLoadModule mpm_worker_module libexec/apache2/mod_mpm_worker.so"

echo "\n* Add following line in the start of section with LoadModule instructions"

echo "\nLoadModule mpm_prefork_module libexec/apache2/mod_mpm_prefork.so"

echo "\nTo enable PHP, add these lines to `/data/data/com.termux/files/home/etc/apache2/httpd.conf`:"

echo "\n* Place this at the end of the LoadModule list:

nano /data/data/com.termux/files/home/etc/apache2/httpd.conf

LoadModule php7_module libexec/apache2/libphp7.so

AddHandler php7-script .php

echo "\n* Place this at the end of the Include list (this will be at the end of file):"

mkdir etc/

mkdir etc/apache2/

mkdir etc/apache2/extra/

touch etc/apache2/extra/php7_module.conf

Include etc/apache2/extra/php7_module.conf

echo "\nTo test if php works:"

echo "\n* Create index.php file with arbitrary content"

echo '<?php phpinfo();?>' > /data/data/com.termux/files/usr/share/apache2/default-site/htdocs/index.php

echo "\n* Restart apache2 server"

killall httpd; httpd

echo "\n* Verify PHP output"

curl 127.0.0.1:8080/index.php
