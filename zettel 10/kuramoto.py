# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:57:30 2015

@author: eric.bertok
"""

import scipy.integrate as sp
import matplotlib.pyplot as plt
import numpy as np
import time


#Parameters:
N=10
stdev=0.1
K=10
timee=1000
dt=0.1
#K=np.linspace(0,10,100)

array=np.empty(N)
omega=np.empty(N)
X=np.empty(N)
x_0=2*np.pi*np.random.random(size=N)
result=np.array([x_0,x_0])
R=np.abs(1/float(N)*np.sum(np.exp(1.j*X)))
theta=np.angle(1/float(N)*np.sum(np.exp(1.j*X)))

for i in range(N):
    omega[i]=np.random.normal(loc=1,scale=stdev)
    array[i]=(omega[i]+K*np.sin(theta-X[i]))%(2*np.pi)

#Set Diff. Equation:
def Sys(t,X):    
    return np.array(np.fromiter(array,float))

#integrate and check function:
def integrieren(x_0,result,timee,dt=0.1):
    r=sp.ode(Sys) 
    r.set_integrator('dopri5')
    r.set_initial_value(x_0)
    while r.t<timee:
        print 'test'
        X=r.integrate(r.t+dt)
        np.append(result,X)
    return result

start = time.time()
########################################################

result2=integrieren(x_0,result,timee,dt)

fig=plt.figure()
x=np.empty(N)
#for j in range(int(timee/dt)):
 #   x.fill(j)
 #   plt.plot(result[j],x)
########################################################
x.fill(1)
print x
print result2[199]
stop = time.time()
print stop-start,'\t'


    