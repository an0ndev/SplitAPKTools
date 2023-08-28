from utils import run_sys

import sys


PACKAGE_ID = sys.argv[1]

apk_paths = [
    path[len("package:"):]
    for path in run_sys(f"adb shell pm path {PACKAGE_ID}", get_output=True)
    .split("\n")[:-1]
]
for APK_PATH in apk_paths:
    run_sys(f"adb pull {APK_PATH}")
