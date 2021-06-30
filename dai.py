from thinkdsp import Chirp
from thinkdsp import normalize, unbias
import numpy as np
from thinkdsp import decorate
from matplotlib import colors
#from scipy.singal.filter_degin import freqs
import matplotlib.pyplot as plt
PI2 = 2 * np.pi

class SawtoothChirp(Chirp):
    

    def evaluate(self,ts):
      
        freqs = np.linspace(self.start, self.end, len(ts))
        dts=np.diff(ts,prepend=0)
        
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys
signal=SawtoothChirp(start=220,end=880)
wave=signal.make_wave(duration=0.1,framerate=4000)
wave.apodize()
wave.write(filename="output3-2.wav")
plt.subplot(1,2,1)
plt.title("SawtoothChirp")
wave.plot()

sp=wave.make_spectrum(256)
plt.subplot(1,2,2)
sp.plot()
plt.xlabel("时间")
plt.ylabel("频率")
plt.title("频谱")
plt.show()