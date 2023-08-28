# Split APK Tools
## Prereqs
- python with BeautifulSoup4 (+ parser) and wrapt (`pip install BeautifulSoup4 lxml wrapt`)
- up-to-date [apktool](https://apktool.org) on PATH
- adb on PATH with target device connected (root not required)
- Android SDK Build Tools (Android\Sdk\build-tools\<version>) on PATH
## Usage
- install desired app on target device (eg from play store)
- `python PREPARE.py com.my.package`: pulls split apk, combines into `base` folder, applies network security config patch and some fixes, saves package name in `package_name.txt`
- edit code or resources in `base` directory
- `python SEND.py`: repackages, signs, and installs apk (uninstalls current version, then installs modded apk)
- `python CLEAN.py`: removes temporary files to prepare for modding new app
## Acknowledgements
- https://github.com/levyitay/AddSecurityExceptionAndroid
- XDA developers forums, page explaining the fixes

