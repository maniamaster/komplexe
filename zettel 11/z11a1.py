import numpy as np
import scipy as sp
import matplotlib as mt
import scipy.integrate as int
# mt.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import *
import sys
import time

# params:
N = 100000
x0 = 0.3

start = time.time()


def tent(x):
    if x < 0.5:
        return (2*x*np.random.normal(loc=1, scale=1e-4)) % 1
    else:
        return (2*(1-x)*np.random.normal(loc=1, scale=1e-4)) % 1

x = x0
arr = np.array([x0])
for i in range(N):
    x = tent(x)
    arr = np.append(arr, x)

fourier = np.fft.fft(arr)

fig = plt.figure()
axx = np.linspace(0, 1, 1000)
freqn   = np.fft.fftfreq(np.int(N+1))
plt.plot(freqn[np.nonzero(freqn)],fourier[np.nonzero(freqn)], 'b,')
plt.title('N='+str(N))
plt.show()
#plt.savefig('N='+str(N)+'.png',dpi=500)

stop = time.time()
# print stop-start'\t'
