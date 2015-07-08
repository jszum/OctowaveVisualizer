#!/usr/bin/env python

from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sys

class Vis:

    def __init__(self, filename=None):
        self.numberOfPlots = 2
        self.figurePerPlot = 4
        self.filename = filename

    def show(self):
        for plot in range(self.numberOfPlots):
            plt.figure(plot)
            plt.waitforbuttonpress()

            for fig in range(self.figurePerPlot):
                input_data = read(self.filename)
                audio = input_data[1]

                plt.subplot(2, 2, fig + 1)
                plt.plot(audio[0:-1])
                plt.ylabel("Amplitude")
                plt.xlabel("Time")
                plt.title("Channel " + str(plot * self.figurePerPlot + fig))

            mng = plt.get_current_fig_manager()
            mng.resize(*mng.window.maxsize())
            plt.show()

if __name__ == '__main__':
    print(' '.join(sys.argv))
    name = sys.argv[1]
    visualiser = Vis(name)
    visualiser.show()


