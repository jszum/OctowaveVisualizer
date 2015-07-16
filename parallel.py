#!/usr/bin/env python

import subprocess
import sys

name = sys.argv[1]
option = int(sys.argv[2])

vis = ''

if option == 0:
    vis = "./waveform.py"
else:
    vis = "./fftplayer.py"

subprocess.Popen([vis, name])
subprocess.call(["./player.py", name])
