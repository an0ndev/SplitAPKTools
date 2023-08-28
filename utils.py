import sys
import subprocess


def run_py(py_file: str, *args: str):
    subprocess.check_call([sys.executable, py_file, *args], shell=False)


def run_sys(cmd: str, get_output: bool = False) -> str:
    if get_output:
        func = subprocess.check_output
    else:
        # Avoid capturing output when not necessary,
        # so it can be read by user
        func = subprocess.check_call
    return func(cmd, shell=True, text=True)
