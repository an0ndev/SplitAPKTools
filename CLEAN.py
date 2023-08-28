import pathlib
import shutil


package_name_file = pathlib.Path("package_name.txt")
if package_name_file.exists():
    package_name_file.unlink()


for f in pathlib.Path.cwd().glob("*.apk"):
    f.unlink()
    apk_name = pathlib.Path.cwd() / f.name.rpartition(".")[0]
    if apk_name.exists():
        shutil.rmtree(apk_name)

for f in pathlib.Path.cwd().glob("out*"):
    f.unlink()
