# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:57:30 2015

@author: eric.bertok
"""

import scipy.optimize as spopt
import scipy.integrate as spint
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import time
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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

#Shinriki:
R1min=19.
R1max=22.
C1=0.01
C2=0.1
L=0.32
R2=14.5
R3=0.1
RINC=6.9
a=2.295e-5
b=3.0038


def line(t):
    global x1,x2
    return x1+t*(x2-x1)

#logistic function:
def logistic(r,x):
    return r*x*(1-x)
    
#DiffEquation:
def Sys(t,X):
    global C1,C2,L,R1,R2,R3,RINC,a,b
    return np.array([1/C1*(X[0]*(1/RINC-1/R1)-a*(exp(b*(X[0]-X[1]))-exp(-b*X[0]+b*X[1]))-(X[0]-X[1])/R2),
                     1/C2*(a*(exp(b*(X[0]-X[1]))-exp(-b*X[0]+b*X[1]))+(X[0]-X[1])/R2-X[2]),
                     1/L*(-X[2]*R3+X[1])])


#def array:
array_r=np.linspace(rmin,rmax,n_r)
array_x=np.linspace(xmin,xmax,n_x)

#integrator:
def integrieren(x_0,y_0,z_0,dt=0.01):
    global intx,inty,intz,poinx,poiny,poinz,x1,x2          
    r=spint.ode(Sys) 
    r.set_integrator('dopri5')
    r.set_initial_value([x_0,y_0,z_0])
    X=[0,0,0]   
    while r.t<50:
        X=r.integrate(r.t+dt)   
    while r.t<200:     
        Xbefore=X        
        X=r.integrate(r.t+dt)     
        intx=np.append(intx,X[0])
        inty=np.append(inty,X[1])   
        intz=np.append(intz,X[2])        
        if X[1]-Xbefore[1]<0 and X[1]*Xbefore[1]<0:
            x1=Xbefore[1]            
            x2=X[1]
            root=spopt.brentq(line,100,-100)
            poinx=np.append(poinx,Xbefore[0]+root*(X[0]-Xbefore[0]))
            poiny=np.append(poiny,Xbefore[1]+root*(X[1]-Xbefore[1]))  
            poinz=np.append(poinz,Xbefore[2]+root*(X[2]-Xbefore[2]))
    return intx,inty,intz,poinx,poiny,poinz
    
def bifurcation():
    global array_r,array_x
    for r in array_r:
        for x in array_x:
            for t in range(0,ttrans,1):
                x=logistic(r,x)
                for t in range(0,tlimit,1):
                    x=logistic(r,x)
                    plt.plot(r,x,'bo',ms=0.5,linestyle='None')
                    
def integrierenbif(x_0,y_0,z_0,dt=0.01):
    global x1,x2,fig,R1       
    r=spint.ode(Sys) 
    r.set_integrator('dopri5')
    r.set_initial_value([x_0,y_0,z_0])
    X=[0,0,0]   
    while r.t<50:
        X=r.integrate(r.t+dt)   
    while r.t<200:     
        Xbefore=X        
        X=r.integrate(r.t+dt)     
        if X[1]-Xbefore[1]<0 and X[1]*Xbefore[1]<0:
            x1=Xbefore[1]            
            x2=X[1]
            root=spopt.brentq(line,100,-100)
            plt.plot(R1,Xbefore[0]+root*(X[0]-Xbefore[0]),'bo',ms=0.5,linestyle='none')
    
def bifurcation():
    global array_r,array_x
    for r in array_r:
        for x in array_x:
            for t in range(0,ttrans,1):
                x=logistic(r,x)
                for t in range(0,tlimit,1):
                    x=logistic(r,x)
                    plt.plot(r,x,'bo',ms=0.5,linestyle='None')                    
                    
    
intx=np.array([])
inty=np.array([])
intz=np.array([])
poinx=np.array([])
poiny=np.array([])
poinz=np.array([])




############################################################################
start = time.time() #START

#########Bifurcation Diagram:


fig=plt.figure()
R1a=linspace(R1min,R1max,100)
for R1 in R1a:
	integrierenbif(x_0=1,y_0=1,z_0=1)


######## poincare plot:
poinx=np.array([])
poiny=np.array([])
poinz=np.array([])

fig2=plt.figure()
ax = fig2.add_subplot(111, projection='3d')
R1=22.0
poincare_x=np.linspace(2,-4,100)
poincare_z=np.linspace(1,2,100)

x,y,z,px,py,pz=integrieren(x_0=1,y_0=1,z_0=1)
ax.plot(xs=x,ys=y,zs=z)
ax.scatter(xs=px,ys=py,zs=pz,color='red')
ax.set_xlabel('V1')
ax.set_ylabel('V2')
ax.set_zlabel('I3')
x = [-5,5,5,-5]
y = [0,0,0,0]
z = [-1,-1,1.5,1.5]
verts = [zip(x, y,z)]
collection=Poly3DCollection(verts,alpha=0.2)
collection.set_facecolor([0.5, 0.5, 1])
ax.add_collection3d(collection)

              
stop = time.time() #STOP
print stop-start,'\t'
###########################################################################


plt.show()

    
