# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:26:18 2015

@author: eric.bertok
"""

import scipy.integrate as sp
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy import stats


#parameters:

lim=500
N=100000
ignore=99000

start = time.time()
############################
data=np.loadtxt('example_data.txt',skiprows=ignore)
I=np.empty(lim)
eps=np.empty(lim)

for i in range(lim):
    epsilon=1/float(i+1)
    hist,xedges,yedges=np.histogram2d(data[:,1],data[:,0],bins=3/epsilon,range=[[-1.5, 1.5], [-1.5, 1.5]])
    hist=hist/float(N-ignore)
    test1=hist
    hist=-hist*np.log2(hist)
    test2=hist
    I[i]=np.nansum(hist)   
    eps[i]=np.log2(1/float(epsilon))
    
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(I, eps)   
    
#plt.plot(data[:,0],data[:,1],'b.',ms=0.1)
plt.title('N='+str(N-ignore))
x=np.linspace(0,100,1000)
plt.plot(slope*x+intercept,x,'r-',label='m='+str(slope))
plt.plot(eps,I)
plt.xlabel('log(1/epsilon)')
plt.ylabel('I')
plt.legend()
############################
stop = time.time()
print stop-start,'\t'