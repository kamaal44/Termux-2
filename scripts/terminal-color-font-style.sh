#!/data/data/com.termux/files/usr/bin/bash

# get directory list
find . -type d -print > dirs$$

# clean up
rm -rf dirs$$
rm -rf revdirs$$
