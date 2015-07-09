#!/usr/bin/env python

from scipy.io.wavfile import read
from scipy.fftpack import fft, fftfreq
import scipy
import numpy
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':

    print(' '.join(sys.argv))
    name = sys.argv[1]
    samples = int(sys.argv[2])
    input_data = read(name)

    wavfreq = input_data[0]
    print wavfreq

    my_audio = input_data[1]
    audio = my_audio[0:samples]

    normalized = [(element/2**8.)*2-1 for element in audio]

    fft_signal = fft(normalized)

    fft_freq = fftfreq(len(fft_signal), 1.0/wavfreq)

    plt.figure(1)
    plt.subplot(2, 1, 1)
    plt.plot(fft_freq, numpy.abs(fft_signal))
    axes = plt.gca()
    axes.set_xlim([0, 10000])

    plt.subplot(2, 1, 2)
    plt.plot(fft_freq, 10*scipy.log10(fft_signal))
    axes = plt.gca()
    axes.set_xscale('log')
    axes.set_xlim([0, 10000])

    plt.show()


