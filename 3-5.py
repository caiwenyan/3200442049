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

PI2=2*np.pi
class TromboneGliss(Chirp):
    def evaluate(self, ts):
        f1, f2=1.0/self.start,1.0/self.end
        lengths=np.linspace(f1,f2,len(ts))
        freqs=1/lengths

        dts=np.diff(ts,prepend=0)
        dphis=PI2*freqs*dts
        phases=np.cumsum(dphis)
        ys=self.amp*np.cos(phases)
        return ys
        
low=262
high=349
signal=TromboneGliss(high,low)
wave1=signal.make_wave(duration=1)
wave1.apodize()
wave1.write(filename="output3-5-1.wav")

signal=TromboneGliss(high,low)
wave2=signal.make_wave(duration=1)
wave2.apodize()
wave2.write(filename="output3-5-2.wav")

wave=wave1|wave2
wave.write(filename="output3-5-3.wav")

sp=wave.make_spectrum(1024)
sp.plot(high=1000)
plt.title("频率")
plt.show()