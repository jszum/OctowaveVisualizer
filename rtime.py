#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io.wavfile import read
import sys


class PlotLine:

    def __init__(self, name, interval=1000):
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(1,1,1)
        self.counter = 0

        self.wavfile = name
        self.interval = interval

        self.load_data()

        self.samples_per_plot = self.sample_rate * interval/1000

        self.ylimit = max(self.audio)

    def load_data(self):
        input_data = read(self.wavfile)
        self.sample_rate = input_data[0]
        self.audio = input_data[1]

    def animate(self, i):
        current_start = self.counter * self.samples_per_plot
        current_end = (self.counter+1) * self.samples_per_plot

        yar = self.audio[current_start: current_end]
        xar = []

        length = len(yar)
        for i in range(length):
            xar.append(i)

        self.ax.clear()
        self.ax = plt.gca()
        self.ax.set_xlim(0, self.samples_per_plot)

        limit = self.ylimit

        self.ax.set_ylim(-limit, limit)
        self.ax.plot(xar, yar)
        self.counter += 1

    def run(self):
        ani = animation.FuncAnimation(self.figure, self.animate, interval=self.interval)
        plt.show()

if __name__ == '__main__':
    print(' '.join(sys.argv))
    name = sys.argv[1]

    plot = PlotLine(name)
    plot.run()
