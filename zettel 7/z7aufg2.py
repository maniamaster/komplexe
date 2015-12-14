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
iters=16
anzx=25
anzy=25
phaseiters=20

#Map:
def stand(X,K):
    return np.array([(X[0]+X[1])%1,
                     (X[1]+K/(2*np.pi)*np.sin(2*np.pi*(X[0]+X[1]))+1)%2-1])
    
def standback(X,K):
    return np.array([(X[0]-(X[1]-K/(2*np.pi)*np.sin(2*np.pi*(X[0]))))%1,
                     (X[1]-K/(2*np.pi)*np.sin(2*np.pi*(X[0]))+1)%2-1])

def EV1(K):
    return np.array([1,(2+K)/2.+1/2.*np.sqrt(K**2+4*K)])

def EV2(K):
    return np.array([1,(2+K)/2.-1/2.*np.sqrt(K**2+4*K)])


start = time.time()
############################

fig=plt.figure()
a=np.linspace(-10e-6,10e-6,2000)

##plot phase portrait:
for i in range(anzx):
    for j in range(anzy):
            x=np.array([i*1/float(anzx),j*1/float(anzy)])       
            for m in range(phaseiters):
                x=stand(X=x,K=K) 
                plt.plot(x[0],x[1],'k.',ms=0.3)

### plot mannigfaltigkeit
for a in a:
    x1=a*EV1(K)
    x2=a*EV2(K)
    for i in range(iters):
        x2=standback(X=x2,K=K)
        plt.plot(x2[0],x2[1],'b.',ms=1)
        x1=stand(X=x1,K=K)
        plt.plot(x1[0],x1[1],'r.',ms=1)




plt.title('K=0.5')
plt.xlim(0,1)
plt.ylim(-1,1)
plt.xlabel('x')
plt.ylabel('p')



############################
stop = time.time()
print stop-start,'\t'


    