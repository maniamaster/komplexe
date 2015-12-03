# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:18:28 2015

@author: eric.bertok
"""

import scipy.integrate as sp
import matplotlib.pyplot as plt
import numpy as np
import time
import math

##parameters:
n=1000
rmin=2.
rmax=4.
nr=10000.
x0=0.4



def logistic(r,x):
    return r*x*(1-x)

def lya(r,n,x0):
    l=0
    x=np.empty(n)
    x[0]=x0
    for i in range(n-1):
        x[i+1]=logistic(r,x[i])
        if r*(1-2*x[i])==0:
            l+=float("inf")
        else:
            l+=1/float(n)*np.log(abs(r*(1-2*x[i])))
    return l
    


start=time.time()
#####################
r_range=np.linspace(rmin,rmax,nr)
fig=plt.figure()
for r in r_range:
    x=r
    y=lya(r,n,x0)
    plt.plot(x,y,'bo',ms=0.5)
plt.xlim(2,4)
plt.ylim(-2,1)
plt.xlabel('r')
plt.ylabel('lambda')




#####################
stop=time.time()
print stop-start