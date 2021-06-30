from matplotlib import colors
from scipy.signal.filter_design import freqs
from thinkdsp import Chirp, decorate, read_wave
from thinkdsp import normalize,unbias
import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal
import wave


plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号

wave=read_wave('120994__thirsk__120-oboe.wav')
wave.write(filename="output3-4.wav")


plt.title("音频")
wave.make_spectrum(512).plot(high=5000)
plt.show()