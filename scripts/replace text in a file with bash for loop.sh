#!/data/data/com.termux/files/usr/bin/bash

OLD="#!/data/data/com.termux/files/usr/bin/python3"
NEW="#!@TERMUX_PREFIX@/bin/python3"
DPATH="/sdcard/github/Termux/python/*.py"
BPATH="/sdcard/github/Termux/bup"
TFILE="/data/data/com.termux/files/tmp/out.tmp.$$"
[ ! -d $BPATH ] && mkdir -p $BPATH || :
for f in $DPATH
do
  if [ -f $f -a -r $f ]; then
    /bin/cp -f $f $BPATH
   sed "s/$OLD/$NEW/g" "$f" > $TFILE && mv $TFILE "$f"
  else
   echo "Error: Cannot read $f"
  fi
done

cp -R /sdcard/github/Termux/bup/ /sdcard/github/Termux/python

rm -rf "$TFILE" /sdcard/github/Termux/bup
