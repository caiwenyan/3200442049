# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 08:42:58 2021

@author: admin
"""
#import Audio from IPython.display
from thinkdsp import SquareSignal, decorate
import matplotlib.pyplot as plt
signal = SquareSignal(1100)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
#plt.subplot(1,2,1)
segment.plot()
decorate(xlabel='Time (s)')
# wave = signal.make_wave(duration=0.5, framerate=10000)
# #wave.apodize()

# spectrum = wave.make_spectrum()
# plt.subplot(1,2,2)
# spectrum.plot()
# #decorate(xlabel='Frequency (Hz)')
