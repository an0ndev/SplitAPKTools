set -e

base_dir="base"
out_file="out.apk"
out_file_signed="out_signed.apk"
out_file_aligned="out_aligned.apk"
debugKeystore="${HOME}/.android/debug.keystore"
if [ ! -f $debugKeystore ]; then
      if [ ! -d ~/.android ]; then
        mkdir ~/.android
      fi
      echo "No debug keystore was found, creating new one..."
      keytool -genkey -v -keystore $debugKeystore -storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000
fi

apktool empty-framework-dir --force "$base_dir"
echo "Building temp APK $out_file"
apktool b --use-aapt2 -o "./$out_file" "$base_dir"
rm -f $out_file_aligned
zipalign -p 4 $out_file $out_file_aligned
rm -f $out_file_signed
apksigner sign --ks "$debugKeystore" --in "./$out_file_aligned" --out "./$out_file_signed" --ks-pass pass:android --key-pass pass:android # androiddebugkey?
echo "done: $out_file_signed"
