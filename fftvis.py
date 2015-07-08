#!/usr/bin/env python

from scipy.io.wavfile import read
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':

    print(' '.join(sys.argv))
    name = sys.argv[1]
    samples = int(sys.argv[2])
    input_data = read(name)

    myaudio = input_data[1]
    audio = myaudio[0:samples]

    normalized =[(ele/2**8.)*2-1 for ele in audio]

    fft_signal = fft(normalized)
    d = len(fft_signal)/2
    plt.plot(abs(fft_signal[:(d-1)]), 'r')
    plt.show()


