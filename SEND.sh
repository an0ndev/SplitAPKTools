set -e

./repack.sh
adb push out_signed.apk
