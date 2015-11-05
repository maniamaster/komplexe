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
gamma=1





#Set Diff. Equation:
def Sys(t,X):
    return np.array([X[1],X[0]-X[0]**3-gamma*X[1]])

#integrate and check function:
def integrieren(x,v,dt=0.1):
    r=sp.ode(Sys) 
    r.set_integrator('dopri5')
    r.set_initial_value([x,v])
    E = 1 #Energy
    while E>0:
        X=r.integrate(r.t+dt)
        E=0.5*X[1]**2-0.5*X[0]**2+0.25*X[0]**4
    if E==0:
        fix=0
    else:
        if X[0]>0:
            fix=1
        else:
            fix=-1
    return fix



maxx = 10
minx = -10
minxp = -25
maxxp = 25

genau = 2

X,Y = np.mgrid[minx:maxx+1/float(genau):1/float(genau),minxp:maxxp+1/float(genau):1/float(genau)]
A = np.zeros(((maxx-minx)*genau,(maxxp-minxp)*genau))

start = time.time()
for i in range(0,(maxx-minx)*genau):
	for j in range(0,(maxxp-minxp)*genau):
		A[i][j] = integrieren(x=X[i][0],v=Y[0][j])

		
stop = time.time()
print stop-start,'\t',gamma

plt.ioff()
#fig = figure()
plt.pcolor(X,Y,A, cmap='seismic')
#plt.colorbar()
plt.axes([minx,maxx,minxp,maxxp])
plt.show()

    