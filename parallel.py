#!/usr/bin/env python
import subprocess
import sys

name = sys.argv[1]

subprocess.Popen(["./fftplayer.py", name])
subprocess.call(["./player.py", name])