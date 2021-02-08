#!/bin/bash

OLD="echo"
NEW="echo"
DPATH="/e/github/nw/Termux/installs/*.sh"
BPATH="/e/github/nw/Termux/bakup/"
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

rm -rf "$TFILE"
