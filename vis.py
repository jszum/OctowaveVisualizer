#!/usr/bin/env python

from scipy.fftpack import fft, fftfreq
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy
import scipy
import sys

class Vis:

    def __init__(self, filename=None, samples=-1, option=0):
        self.numberOfPlots = 1
        self.figurePerPlot = 8
        self.filename = filename
        self.samples = samples
        self.option = option

    def show(self):
        plt.figure(1)

        for plot in range(self.numberOfPlots):

            for fig in range(self.figurePerPlot):
                current_plot = plot * self.figurePerPlot + fig
                input_data = read(self.filename[:-5] + str(current_plot) + '.wav')
                audio = input_data[1]

                if self.option == 0:
                    plt.subplot(4, 2, fig + 1)
                    plt.plot(audio[0:self.samples])
                    plt.title("Channel " + str(current_plot))

                else:
                    normalized = [(element/2**8.)*2-1 for element in audio[0:self.samples]]
                    fft_signal = fft(normalized)
                    fft_freq = fftfreq(len(fft_signal), 1.0/input_data[0])
                    plt.subplot(4, 2, fig + 1)
                    plt.plot(fft_freq, 10*scipy.log10(fft_signal))
                    axes = plt.gca()
                    axes.set_xscale('log')
                    axes.set_xlim([0, self.samples])
                    plt.title("FFT channel " + str(current_plot))

        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()

if __name__ == '__main__':
    print(' '.join(sys.argv))
    name = sys.argv[1]
    samples = int(sys.argv[2])
    option = int(sys.argv[3])
    visualiser = Vis(name, samples, option)
    visualiser.show()


