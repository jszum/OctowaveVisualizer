#!/usr/bin/env python

from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sys

file = sys.argv[1]

numberOfPlots = 2
figurePerPlot = 4
f = 0

for plot in range(numberOfPlots):
    plt.figure(plot)
    plt.waitforbuttonpress()

    for fig in range(figurePerPlot):
        input_data = read(file)
        audio = input_data[1]

        plt.subplot(2, 2, fig + 1)
        plt.plot(audio[0:-1])
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.title("Channel " + str(plot * figurePerPlot + fig))

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()



