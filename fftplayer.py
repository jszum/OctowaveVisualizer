#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io.wavfile import read
from scipy.fftpack import fft, fftfreq
import scipy
import numpy
import sys


class PlotLine:

    def __init__(self, name, interval=1000):
        self.figure = plt.figure()
        self.counter = 0
        self.interval = interval

        self.load_data(name)

        self.samples_per_plot = self.sample_rate * interval/1000
        self.ax = self.figure.add_subplot(1, 1, 1)

        self.limit = 110000
        self.figure.canvas.mpl_connect('key_press_event', self.scaling)

    def load_data(self, wavfile):
        input_data = read(wavfile)
        self.sample_rate = input_data[0]
        self.audio = input_data[1]

    def scaling(self, event):
        if event.key == '=':
            self.limit += 100000
        if event.key == '-':
            self.limit -= 100000

        if self.limit < 0:
            self.limit = 10000

        print('Yaxis max:', self.limit)

    def animate(self, i):
        current_start = self.counter * self.samples_per_plot
        current_end = (self.counter+1) * self.samples_per_plot

        self.ax.clear()
        self.ax = plt.gca()

        normalized = []
        fft_signal = []
        fft_freq = 0

        normalized = [(element/2**8.)*2-1 for element in self.audio[current_start: current_end]]
        fft_signal = fft(normalized)
        fft_freq = fftfreq(len(fft_signal), 1.0/self.sample_rate)

        self.ax.set_ylim(0, self.limit)
        self.ax.set_xlim(0, self.samples_per_plot/2)

        plt.plot(fft_freq[200:], abs(fft_signal[200:]))
        axes = plt.gca()
        axes.set_xscale('linear')
        self.counter += 1

    def run(self):
        ani = animation.FuncAnimation(self.figure, self.animate, interval=850)
        plt.show()

if __name__ == '__main__':
    print(' '.join(sys.argv))
    name = sys.argv[1]

    plot = PlotLine(name)
    plot.run()
