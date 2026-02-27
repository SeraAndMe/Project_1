#!/usr/bin/env python3
# 烧录脚本

import sys
import os

if len(sys.argv) != 2:
    print("Usage: python flash.py <bin_file>")
    sys.exit(1)

bin_file = sys.argv[1]

print(f"Flashing {bin_file}...")
# 这里添加实际的烧录逻辑
print("Flash completed successfully!")
