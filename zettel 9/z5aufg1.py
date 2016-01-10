# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:57:30 2015

@author: eric.bertok
"""

import scipy.integrate as sp
import matplotlib.pyplot as plt
import numpy as np
import time
from mpl_toolkits.mplot3d import Axes3D


#Parameters:
#bifurcation:
rmin=2.9
rmax=4
n_r=1000
xmin=0
xmax=1
n_x=10
ttrans=1000
tlimit=20


#logistic function:
def logistic(r,x):
    return r*x*(1-x)
    

#def array:
array_r=np.linspace(rmin,rmax,n_r)
array_x=np.linspace(xmin,xmax,n_x)

    

    



fig=plt.figure()
plt.title('Bifurcation Diagram ttrans=10000')
plt.xlabel('r')
plt.ylabel('x_s')

fig2=plt.figure()
ax = fig.add_subplot(111, projection='3d')

start = time.time() #START

for r in array_r:
        for x in array_x:
            for t in range(0,ttrans,1):
                x=logistic(r,x)
                for t in range(0,tlimit,1):
                    x=logistic(r,x)
                    plt.plot(r,x,'bo',ms=0.5,linestyle='None')  

stop = time.time() #STOP
print stop-start,'\t'


plt.show()

    