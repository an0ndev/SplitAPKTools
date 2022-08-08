# Split APK Tools
## Prereqs
- python with BeautifulSoup4
- up-to-date apktool on PATH
- adb on PATH with target device connected (root not required)
## Usage
- install desired app on target device (eg from play store)
- `./PREPARE.sh com.my.package`: pulls split apk, combines into `base` folder, applies network security config patch and some fixes
- edit code or resources in `base` directory
- `./SEND.sh`: repackages, signs, and pushes apk
- `./CLEAN.sh`: removes temporary files to prepare for modding new app
## Acknowledgements
- https://github.com/levyitay/AddSecurityExceptionAndroid
- XDa developers forums, page explaining the fixes
