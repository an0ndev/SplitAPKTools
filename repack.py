from utils import run_sys

import pathlib


home = pathlib.Path.home()

base_dir = pathlib.Path("base")
out_file = pathlib.Path("out.apk")
out_file_signed = pathlib.Path("out_signed.apk")
out_file_aligned = pathlib.Path("out_aligned.apk")
debugKeystore = home / ".android" / "debug.keystore"

if not debugKeystore.is_file():
    if not (home / ".android").is_dir():
        (home / ".android").mkdir()
    print("No debug keystore was found, creating new one...")
    run_sys(
        f"keytool -genkey -v "
        f"-keystore {debugKeystore} "
        f"-storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000"
    )

run_sys(f"apktool empty-framework-dir --force {base_dir}")
print(f"Building temp APK {out_file}")
run_sys(f"apktool b --use-aapt2 -o {out_file} {base_dir}")
out_file_aligned.unlink(missing_ok=True)
run_sys(f"zipalign -p 4 {out_file} {out_file_aligned}")
out_file_signed.unlink(missing_ok=True)
run_sys(f"apksigner sign "
        f"--ks {debugKeystore} "
        f"--in {out_file_aligned} "
        f"--out {out_file_signed} "
        f"--ks-pass pass:android "
        f"--key-pass pass:android")
print(f"done: {out_file_signed}")
