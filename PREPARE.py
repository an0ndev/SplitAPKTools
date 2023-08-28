from utils import run_py

import sys
import pathlib


run_py("pull.py", sys.argv[1])
run_py("unpack.py")
run_py("merge_resources.py")
run_py("patch_network.py")
run_py("remove_split_apk_attrib.py")

pathlib.Path("package_name.txt").write_text(sys.argv[1])
