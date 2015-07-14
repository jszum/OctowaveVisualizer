#!/usr/bin/env python
import subprocess
import sys

name = sys.argv[1]

subprocess.Popen(["./rtime.py", name])
subprocess.call(["./octo.py", name])