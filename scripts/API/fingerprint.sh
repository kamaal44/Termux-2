#!/data/data/com.termux/files/usr/bin/sh
set -e -u

SCRIPTNAME=termux-fingerprint
show_usage () {
    echo "Usage: $SCRIPTNAME [-t title] [-d description] [-s subtitle] [-c cancel]"
    echo "Use fingerprint sensor on device to check for authentication"
    echo "NOTE: Only available on Marshmallow and later"
    exit 0
}

ARG_T=""
OPT_T=""
ARG_D=""
OPT_D=""
ARG_S=""
OPT_S=""
ARG_C=""
OPT_C=""

while getopts :ht:d:s:c: option
do
    case "$option" in
        h) show_usage;;
        t) ARG_T="--es title";OPT_T="$OPTARG";;
        d) ARG_D="--es description";OPT_D="$OPTARG";;
        s) ARG_S="--es subtitle";OPT_S="$OPTARG";;
        c) ARG_C="--es cancel";OPT_C="$OPTARG";;
        ?) echo "$SCRIPTNAME: illegal option -$OPTARG"; exit 1;
    esac
done

set --
if [ -n "$ARG_T" ]; then set -- "$@" $ARG_T "$OPT_T"; fi
if [ -n "$ARG_D" ]; then set -- "$@" $ARG_D "$OPT_D"; fi
if [ -n "$ARG_S" ]; then set -- "$@" $ARG_S "$OPT_S"; fi
if [ -n "$ARG_C" ]; then set -- "$@" $ARG_C "$OPT_C"; fi

/data/data/com.termux/files/usr/libexec/termux-api Fingerprint "$@"
