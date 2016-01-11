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
omegamin=0
omegamax=2
n_omega=10000
ttrans=100000
tlimit=10
K=0.9

#logistic function:
def circle(omega,theta,K):
    return theta+omega-K/(2*np.pi)*np.sin(2*np.pi*theta)
    


start = time.time() #START
##################################################################

array_omega=np.linspace(omegamin,omegamax,n_omega)
fig=plt.figure()
plt.title('Bifurcation Diagram, t_trans=' +str(ttrans))
plt.xlabel('Omega')
plt.ylabel('theta_s')
theta=np.empty(n_omega)
theta.fill(1)
theta_in=theta
winding=np.empty(n_omega)
lyap=np.empty(n_omega)

for t in range(0,ttrans,1):
   theta=circle(array_omega,theta,K)
   lyap+=np.log(np.abs(1-K*np.cos(2*np.pi*theta)))
for t in range(0,tlimit,1):
   theta=circle(array_omega,theta,K)
   plt.plot(array_omega,theta,'bo',ms=0.5,linestyle='None')  
   lyap+=np.log(np.abs(1-K*np.cos(2*np.pi*theta)))

winding=(theta-theta_in)/float(ttrans+tlimit)
fig2=plt.figure()
plt.title('Winding number ttrans+tlimit='+str(ttrans+tlimit))
plt.xlabel('Omega')
plt.ylabel('winding number')
plt.plot(array_omega,winding)

lyap=lyap/float(ttrans+tlimit)
fig3=plt.figure()
plt.title('lyapunov exponent ttrans+tlimit='+str(ttrans+tlimit))
plt.xlabel('Omega')
plt.ylabel('lambda')
plt.plot(array_omega,lyap)
###################################################################                    
stop = time.time() #STOP
print stop-start,'\t'


plt.show()

    