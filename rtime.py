#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io.wavfile import read
import sys

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

name = sys.argv[1]

input_data = read(name)

sample_rate = input_data[0]
print sample_rate
audio = input_data[1]
counter = 0
lim = max(audio)

rate = sample_rate
interval = 1000


samples = rate * interval/1000
print samples
def animate(i):
    global counter
    global lim
    global rate

    xar = []

    yar = audio[counter * samples: (counter+1)*samples]

    length = len(yar)
    for i in range(length):
        xar.append(i)

    ax1.clear()
    ax = plt.gca()
    ax.set_xlim(0, samples)
    ax.set_ylim(-lim, lim)
    ax1.plot(xar, yar)
    counter += 1

ani = animation.FuncAnimation(fig, animate, interval=interval)
plt.show()


