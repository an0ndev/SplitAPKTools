set -e

base_dir="base"

apktool d -f $1 -o $base_dir base.apk

for f in *.apk; do
[[ $f == "base.apk" ]] && continue
apkname=${f%.*}
apktool d -f $1 -o $apkname $f
python3 copy_and_add_dnc.py $apkname
done
