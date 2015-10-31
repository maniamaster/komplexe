# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:16:29 2015

@author: eric.bertok
"""
#source: http://systems-sciences.uni-graz.at/etextbook/sw2/phpl_python.html

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# define system in terms of a Numpy array
def Sys(X, t=0):
    # here X[0] = x and x[1] = y    
    return np.array([ (1-X[0])*X[0] - 10*X[0]*X[1] , -1.5*X[1] + 10*X[0]*X[1] ])

# generate 1000 linearly spaced numbers for x-axes
t = np.linspace(0, 50,  2500)
# initial values: x0 = 2, y0 = 6
Sys0 = np.array([0.9, 0.1])

# type "help(integrate.odeint)" if you want more information about integrate.odeint inputs and outputs.
X, infodict = integrate.odeint(Sys, Sys0, t, full_output=True)
# infodict['message']                      # integration successful

x,y = X.T

#plot
fig = plt.figure(figsize=(15,5))
fig.subplots_adjust(wspace = 0.5, hspace = 0.3)
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(x, 'r-', label='prey')
ax1.plot(y, 'b-', label='predator')
ax1.set_title("Dynamics in time")
ax1.set_xlabel("time")
ax1.grid()
ax1.legend(loc='best')

ax2.plot(x, y, color="blue")
ax2.set_xlabel("x")
ax2.set_ylabel("y")  
ax2.set_title("Phase space")
ax2.grid()

# streamplot
# define a grid and compute direction at each point
x_p = np.linspace(0, 2, 20)
y_p = np.linspace(0, 2, 20)

X1 , Y1  = np.meshgrid(x_p, y_p)                    # create a grid
DX1, DY1 = Sys([X1, Y1])                        # compute growth rate on the grid

#plot
fig2 = plt.figure(figsize=(8,6))
ax4 = fig2.add_subplot(1,1,1)

ax4.streamplot(X1, Y1, DX1, DY1)
ax4.legend()
ax4.grid()