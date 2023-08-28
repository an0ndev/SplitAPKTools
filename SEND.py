from utils import run_py, run_sys


import pathlib

package_name = pathlib.Path("package_name.txt").read_text()


run_py("repack.py")
run_sys(f"adb uninstall {package_name}")
run_sys(f"adb install out_signed.apk")
