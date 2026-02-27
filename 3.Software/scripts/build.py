#!/usr/bin/env python3
# 构建脚本

import os
import subprocess

def build():
    print("Building project...")
    result = subprocess.run(["make", "all"], cwd=os.path.dirname(os.path.dirname(__file__)))
    if result.returncode == 0:
        print("Build completed successfully!")
    else:
        print("Build failed!")
        return False
    return True

def clean():
    print("Cleaning project...")
    result = subprocess.run(["make", "clean"], cwd=os.path.dirname(os.path.dirname(__file__)))
    if result.returncode == 0:
        print("Clean completed successfully!")
    else:
        print("Clean failed!")
        return False
    return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        clean()
    else:
        build()
