import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal
#import winsound
#import Audio from IPython.display

#winsound.PlaySound('120994__thirsk__120-oboe.wave',flags=1)


plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号

wave=thinkdsp.read_wave('120994__thirsk__120-oboe.wav')
plt.subplot(2,3,1)
plt.title('原波形')
wave.plot()
wave.write(filename='output1-2.wav')


segment=wave.segment(start=0,duration=0.5)
plt.subplot(2,3,2)
plt.title('截取0.5s后的音频')
segment.plot()


spectrum=wave.make_spectrum()
plt.subplot(2,3,3)
plt.title('频谱')
spectrum.plot()



spectrum.low_pass(cutoff=600,factor=0.01)#将高于600HZ的频段衰减99%
plt.subplot(2,3,4)
plt.title('经过低通滤波器后的频谱')
spectrum.plot()
#wave=spectrum.make_wave()
#wave.play('temp.wave')

spectrum.high_pass(cutoff=600,factor=0.01)#将低于600HZ的频段衰减99%
plt.subplot(2,3,5)
plt.title('经过通高滤波器后的频谱')
spectrum.plot()

spectrum.band_stop(low_cutoff=600,high_cutoff=1000)
plt.subplot(2,3,6)
plt.title('带阻滤波600-1000HZ的频谱')
spectrum.plot()
plt.show()