# -*- coding: utf-8 -*-
"""
Created on Thu Dez  7 16:57:30 2015

@author: eric.bertok
"""

import scipy.integrate as sp
import matplotlib.pyplot as plt
import numpy as np
import time


#Parameters:
K=0.5
iters=1000

#Map:
def stand(X,K):
    return np.array([(X[0]+X[1])%1,(X[1]+K/(2*np.pi)*np.sin(2*np.pi*(X[0]+X[1])))%2])

def EV1(K):
    return np.array([1,(2+K)/2+np.sqrt(K**2+4)])

def EV2(K):
    return np.array([1,(2+K)/2-np.sqrt(K**2+4)])


start = time.time()
############################
x1=0.0001*EV1(K)
x2=0.0001*EV2(K)
plt
for i in range(iters):
    x2=stand(x2,K)
    plt.plot(x2,'b-',ms=1)




############################
stop = time.time()
print stop-start,'\t'


    