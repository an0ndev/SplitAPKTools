from utils import run_py, run_sys

import pathlib


base_dir = pathlib.Path("base")

run_sys(f"apktool d -f -o {base_dir} base.apk")

for f in pathlib.Path.cwd().glob("*.apk"):
    if f.name == "base.apk":
        continue
    apk_name = f.name.rpartition(".")[0]
    run_sys(f"apktool d -f -o {apk_name} {f}")
    run_py("copy_and_add_dnc.py", apk_name)
