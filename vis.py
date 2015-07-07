#!/usr/bin/env python

from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sys

file = sys.argv[1]

input_data = read(file)
audio = input_data[1]

plt.figure(1)
plt.plot(audio[0:-1])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Wav file")

plt.show()