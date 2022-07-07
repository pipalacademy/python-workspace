"""Script to verify if the python-workspace is setup correctly.
"""
import os
import sys
import importlib

def check_system():
    print("Platform:", sys.platform)
    print("Workspace location:", os.getcwd())

def check_python_version():
    v = sys.version_info
    version = f"{v.major}.{v.minor}.{v.micro}"
    print(f"Python version: {version}")

    if v.major != 3:
        fatal("ERROR: Please use Python version 3")

    if v.minor < 7:
        fatal("ERROR: Please use Python version 3.7 or more")

def fatal(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)

def check_package(name):
    try:
        mod = importlib.import_module(name)
    except ImportError:
        fatal(f"{name} not installed. Please look at setup instructions.")

    print(f"{name} version:", mod.__version__)

check_system()
check_python_version()
check_package("pytest")
check_package("jupyterlab")

print()
print("Congratulations! Your workspace is configured correctly.")
