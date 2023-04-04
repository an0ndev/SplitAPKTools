#!/bin/bash
PACKAGE_ID=$1

APK_PATHS=$(adb shell pm path $PACKAGE_ID | cut -c 9-)
for APK_PATH in $APK_PATHS; do
    adb pull $APK_PATH
done
