#!/data/data/com.termux/files/usr/bin/bash

OLD="echo -e"
NEW="echo"
DPATH="/e/github/nw/Termux/scripts/*.txt"
BPATH="/e/github/nw/Termux/bup/"
TFILE="/tmp/out.tmp.$$"
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

cp -R /e/github/nw/Termux/bup/ /e/github/nw/Termux/scripts

rm -rf "$TFILE" /e/github/nw/Termux/bup/
