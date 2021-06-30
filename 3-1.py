import wave
import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal
from thinkdsp import SinSignal, Spectrum, decorate
from thinkdsp import Signal

plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号

signal=SinSignal(freq=440)
duration=signal.period*30.25
wave=signal.make_wave(duration)

for window_func in [np.bartlett,np.blackman,np.hanning,np.hamming]:
    wave=signal.make_wave(duration)
    wave.ys*=window_func(len(wave.ys))
    Spectrum=wave.make_spectrum()
    Spectrum.plot(high=880,label=window_func)



plt.title("频率")
plt.show()