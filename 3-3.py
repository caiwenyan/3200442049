from matplotlib import colors
from scipy.signal.filter_design import freqs
from thinkdsp import Chirp
from thinkdsp import normalize,unbias
import thinkdsp
import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal
import wave


plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号

PI2=2*np.pi
class SawtoothChirp(Chirp):
    def evaluate(self, ts):
        freqs=np.linspace(self.start,self.end,len(ts))
        dts=np.diff(ts,prepend=0)
        dphis=PI2*freqs*dts
        phases=np.cumsum(dphis)
        cycles=phases/PI2
        frac,_=np.modf(cycles)
        ys=normalize(unbias(frac),self.amp)
        return ys

signal=SawtoothChirp(start=2500,end=3000)
wave=signal.make_wave(duration=1,framerate=20000)
wave.write(filename="output3-3.wav")
wave.make_spectrum().plot()
plt.title("频率")
plt.show()
