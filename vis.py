#!/usr/bin/env python

from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sys

class Vis:

    def __init__(self, filename=None, samples=-1):
        self.numberOfPlots = 1
        self.figurePerPlot = 8
        self.filename = filename
        self.samples = samples

    def show(self):
        plt.figure(1)

        for plot in range(self.numberOfPlots):

            for fig in range(self.figurePerPlot):
                current_plot = plot * self.figurePerPlot + fig
                input_data = read(self.filename[:-5] + str(current_plot) + '.wav')
                audio = input_data[1]

                plt.subplot(4, 2, fig + 1)
                plt.plot(audio[0:self.samples])
                # plt.ylabel("Amplitude")
                # plt.xlabel("Time")
                plt.title("Channel " + str(current_plot))

        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()

if __name__ == '__main__':
    print(' '.join(sys.argv))
    name = sys.argv[1]
    samples = int(sys.argv[2])
    visualiser = Vis(name, samples)
    visualiser.show()


