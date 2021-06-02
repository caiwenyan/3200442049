import thinkdsp
import matplotlib.pyplot as plt
from scipy import signal
def strech(wave, fact):
    wave.ts *= fact
    wave.framerate /= fact


plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号

wave=thinkdsp.read_wave('120994__thirsk__120-oboe.wav')
plt.subplot(3,1,1)
plt.title('原信号')
wave.plot()
wave.write(filename='output1-4-1.wav')

strech(wave,0.5)
plt.subplot(3,1,2)
wave.plot()
plt.title('2倍速后的')
wave.write(filename='output1-4-2.wav')


strech(wave,3)
plt.subplot(3,1,3)
wave.plot()
plt.title('0.3倍速后的')
wave.write(filename='output1-4-3.wav')
plt.show()
