#!/usr/bin/env python3

from pathlib import Path
import shlex
import subprocess
import sys
import time

lines = Path(sys.argv[1]).read_text().strip().split('\n')

interval = 0.0
if len(sys.argv) > 2:
    interval = float(sys.argv[2])

for line in lines:
    if len(line) == 0 or line.strip().startswith('#'):
        print(line)
        continue
    else:
        print('$ {}'.format(line))
    try:
        result = subprocess.run(shlex.split(line))
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    if result.returncode != 0:
        sys.exit(result.returncode)
    time.sleep(interval)
