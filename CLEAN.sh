for f in *.apk; do
apkname=${f%.*}
rm -rf $apkname
done
rm -f out*
