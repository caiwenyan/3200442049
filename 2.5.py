import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal
from thinkdsp import SawtoothSignal, SquareSignal, TriangleSignal
from thinkdsp import decorate


plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号

def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0
wave1= TriangleSignal(freq=440).make_wave(duration=0.5)
spectrum1 = wave1.make_spectrum()
filter_spectrum(spectrum1)

spectrum1.scale(440)
plt.subplot(3,3,1)
spectrum1.plot(high=10000, color='blue')
plt.title("三角波频谱")
plt.subplot(3,3,2)
wave1.plot(color='blue')
plt.title('三角波变换前')
plt.subplot(3,3,3)
spectrum1.make_wave().plot(color='blue')
plt.title("三角波变换后")

wave2=SquareSignal(freq=440).make_wave(duration=0.5)
spectrum2 = wave2.make_spectrum()
filter_spectrum(spectrum2)
spectrum2.scale(440)
plt.subplot(3,3,4)
spectrum2.plot(high=10000, color='red')
plt.title("方波")
plt.subplot(3,3,5)
wave2.plot(color='red')
plt.title('方波变换前')
plt.subplot(3,3,6)
spectrum2.make_wave().plot(color='red')
plt.title("方变换后")
spectrum1.make_wave.write(filename='output2-3.wav')


wave3=SawtoothSignal(freq=440).make_wave(duration=0.5)
spectrum3 = wave3.make_spectrum()
filter_spectrum(spectrum3)
spectrum3.scale(440)
plt.subplot(3,3,7)
spectrum3.plot(high=10000, color='green')
plt.title("方波")
plt.subplot(3,3,8)
wave3.plot(color='green')
plt.title('方波变换前')
plt.subplot(3,3,9)
spectrum3.make_wave().plot(color='green')
plt.title("方变换后")
plt.show()


