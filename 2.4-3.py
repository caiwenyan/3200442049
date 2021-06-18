import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal
from thinkdsp import TriangleSignal
from thinkdsp import decorate


plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号

signal= TriangleSignal(freq=440).make_wave(duration=0.01)
#wave=signal.make_wave(duration=0.5 ,framerate=10000)
spectrum = signal.make_spectrum()
spectrum.hs[0]=100
plt.subplot(121)
plt.title('spectrum.hs[0]=100的波形')
spectrum.make_wave().plot()
plt.subplot(122)
signal.plot()
plt.title('原始波形')
plt.show()
