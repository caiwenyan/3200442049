import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal

plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号



signal=thinkdsp.TriangleSignal(200)#200HZ的三角波
wave=signal.make_wave(duration=0.5 ,framerate=10000)#长度0.5，每秒10000次
period=signal.period
segment=wave.segment(start=0,duration=period*3)
plt.subplot(2,2,1)
plt.title('200HZ三角波')
segment.plot()

spectrum=wave.make_spectrum()
plt.subplot(2,2,2)
plt.title('三角波频谱')
spectrum.plot()
#锯齿波
signal1=thinkdsp.SawtoothSignal(200)
wave=signal1.make_wave(duration=0.5 ,framerate=10000)
period=signal1.period
segment=wave.segment(start=0,duration=period*3)
plt.subplot(2,2,3)
plt.title('200HZ锯齿波')
segment.plot()

spectrum=wave.make_spectrum()
plt.subplot(2,2,4)
plt.title('锯齿波频谱')
spectrum.plot()

plt.show()