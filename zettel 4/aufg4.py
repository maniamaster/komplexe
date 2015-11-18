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
a=2

#Set Diff. Equation:
def Sys(t,X):
    return np.array([X[1],-a*X[1]*(X[0]**2+X[1]**2-1)-X[0]])


def integrieren(x,v,dt=0.001):
    global intx
    global inty
    r=sp.ode(Sys) 
    r.set_integrator('dopri5')
    r.set_initial_value([x,v])
    while r.t<20: 
        X=r.integrate(r.t+dt)
        intx=np.append(intx,X[0])
        inty=np.append(inty,X[1])   
    return intx,inty



start = time.time()

intx=np.array([])
inty=np.array([])
x1,y1=integrieren(x=2,v=1.5) 

intx=np.array([])
inty=np.array([])
x2,y2=integrieren(x=0.1,v=0)

intx=np.array([])
inty=np.array([])
x3,y3=integrieren(x=-2,v=0.5)

intx=np.array([])
inty=np.array([])
x4,y4=integrieren(x=0.1,v=3)
		
stop = time.time()
print stop-start,'\t'

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)



#plt.colorbar()

plt.show()

    