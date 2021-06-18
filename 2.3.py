from scipy.signal.spectral import periodogram
import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal

plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号


signal=thinkdsp.SquareSignal(1100)
duration=0.5
wave= signal.make_wave(duration, framerate=10000) 

plt.subplot(1,3,1)
plt.title('1100HZ方波')
wave.plot()
wave.write(filename='output2-3.wav')


spectrum=wave.make_spectrum()
#spectrum=spectrum.mak
plt.subplot(1,3,3)
plt.title('采样后频谱')
spectrum.plot()
plt.show()