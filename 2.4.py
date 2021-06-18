import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal
from thinkdsp import TriangleSignal
from thinkdsp import decorate


plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号

signal=thinkdsp.TriangleSignal(440)
wave=signal.make_wave(duration=0.5 ,framerate=10000)
#period=signal.period
segment=wave.segment(start=0,duration=0.01)
plt.subplot(1,2,1)
plt.title('440HZ三角波')
segment.plot()

spectrum = wave.make_spectrum()
plt.subplot(1,2,2)
plt.title('频谱')
spectrum.plot()

print(spectrum.hs[0])


plt.show()