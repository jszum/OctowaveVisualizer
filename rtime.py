#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io.wavfile import read
import sys


class PlotLine:

    def __init__(self, name, interval=1000):
        self.figure = plt.figure()
        self.counter = 0
        self.interval = interval

        self.load_data(name)

        self.samples_per_plot = self.sample_rate * interval/1000

    def load_data(self, wavfile):
        input_data = read(wavfile)
        self.sample_rate = input_data[0]
        self.audio = input_data[1]

    def animate(self, i):
        ax = self.figure.add_subplot(1, 1, 1)
        current_start = self.counter * self.samples_per_plot
        current_end = (self.counter+1) * self.samples_per_plot

        y_data = self.audio[current_start: current_end]
        x_data = []

        length = len(y_data)
        for i in range(length):
            x_data.append(i)

        ax.clear()
        ax = plt.gca()
        ax.set_xlim(0, self.samples_per_plot)

        limit = max(self.audio)

        ax.set_ylim(-limit, limit)
        ax.plot(x_data, y_data)
        self.counter += 1

    def run(self):
        ani = animation.FuncAnimation(self.figure, self.animate, interval=self.interval)
        plt.show()

if __name__ == '__main__':
    print(' '.join(sys.argv))
    name = sys.argv[1]

    plot = PlotLine(name)
    plot.run()
