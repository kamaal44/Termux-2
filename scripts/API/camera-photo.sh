#!/data/data/com.termux/files/usr/bin/sh
set -e -u

SCRIPTNAME=termux-camera-photo
show_usage () {
    echo "Usage: termux-camera-photo [-c camera-id] output-file"
    echo "Take a photo and save it to a file in JPEG format."
    echo "  -c camera-id  ID of the camera to use (see termux-camera-info), default: 0"
    exit 0
}


PARAMS=""
while getopts :hc: option
do
    case "$option" in
        h) show_usage;;
        c) PARAMS="--es camera $OPTARG";;
        ?) echo "$SCRIPTNAME: illegal option -$OPTARG"; exit 1;
    esac
done
shift $((OPTIND-1))

if [ $# = 0 ]; then echo "$SCRIPTNAME: missing file argument"; exit 1; fi
if [ $# != 1 ]; then echo "$SCRIPTNAME: too many arguments"; exit 1; fi

touch "$1"
PARAMS="$PARAMS --es file `realpath $1`"

/data/data/com.termux/files/usr/libexec/termux-api CameraPhoto $PARAMS
