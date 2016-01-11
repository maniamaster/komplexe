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

def henon(a,b,x):
    return np.array([1-a*x[0]**2+b*x[1],
                     x[0]])
def jac(x):
    return np.array([[-2*a*x[0],b],[1,0]])                    

#parameters:
N=10
a=1.4
b=0.3


start = time.time()
############################





initial=np.array([1,1])
q=np.empty(N+1,dtype=ndarray)
r=np.empty(N+1,dtype=ndarray)
x=initial
q[0]=np.array([[1,0],[0,1]])
r[0]=np.array([[1,0],[0,1]])
arr=jac(x)
for n in range(0,N):
   q[n+1],r[n+1]=np.linalg.qr(np.dot(arr,q[n]))
   D=np.diag([np.sign((r[n+1])[0,0]),np.sign((r[n+1])[1,1])])
   q[n+1]=np.dot(q[n+1],D)
   r[n+1]=np.dot(D,r[n+1])
   x=henon(a,b,x)
   arr=np.dot(jac(x),arr)

lambda1=0
lambda2=0
for n in range(1,N):
    lambda1+=1/float(N)*np.log((r[n][0,0]))
    lambda2+=1/float(N)*np.log((r[n][1,1]))

print 'lambda1: '+ str(lambda1)
print 'lambda2: '+ str(lambda2)
print r[10]


############################
stop = time.time()
print stop-start,'\t'