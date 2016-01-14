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
K=0.2
timee=2000
dt=0.1
anzK=1000
#K=np.linspace(0,10,100)

array=np.empty(N)
omega=np.empty(N)
X=np.empty(N)
x_0=2*np.pi*np.random.random(size=N)
result=np.array([x_0,x_0])
Rresult=np.array([])

print result

omega=np.sort(np.random.normal(loc=1,scale=stdev,size=N))

#Set Diff. Equation:
def Sys(t,X,K,omega):  
    global theta,R
    return np.array(omega+K*np.sin(theta-X))

#integrate and check function:
def integrieren(x_0,result,K,omega,timee,dt=0.1):
    global theta,R
    r=sp.ode(Sys) 
    r.set_integrator('dopri5')
    r.set_f_params(K,omega)
    r.set_initial_value(x_0)
    X=x_0
    while r.t<timee:
        theta=np.angle(1/float(N)*np.sum(np.exp(1.j*X)))  
        R=np.abs(1/float(N)*np.sum(np.exp(1.j*X)))
        X=r.integrate(r.t+dt)
        result=np.append(result,np.array([X]),axis=0)  
        #Rresult=np.append(Rresult,R)
    return result

def Rintegrieren(x_0,Rresult,K,omega,timee,dt=0.1):
    global theta,R
    r=sp.ode(Sys) 
    r.set_integrator('dopri5')
    r.set_f_params(K,omega)
    r.set_initial_value(x_0)
    X=x_0
    while r.t<timee:
        theta=np.angle(1/float(N)*np.sum(np.exp(1.j*X)))  
        R=np.abs(1/float(N)*np.sum(np.exp(1.j*X)))
        X=r.integrate(r.t+dt)
        Rresult=np.append(Rresult,R)
    Rresult=np.sum(Rresult)/(timee/dt)
    return Rresult
    

start = time.time()
########################################################



plt.ion()
Rresult=np.array([])

N=10
fig=plt.figure()
for K in range(anzK):
    Rresult=Rintegrieren(x_0,Rresult,K/float(anzK),omega,timee,dt)  
    K=K/float(anzK)
    plt.plot(K,Rresult,'b.')
    Rresult=np.array([])
plt.title('N= '+str(N)+' , stdev= '+str(stdev))
plt.xlabel('K')
plt.ylabel('<R>')
plt.savefig("stddev=0.1, N={}.png".format(N),dpi=200)

N=100
fig=plt.figure()
for K in range(anzK):
    Rresult=Rintegrieren(x_0,Rresult,K/float(anzK),omega,timee,dt)  
    K=K/float(anzK)
    plt.plot(K,Rresult,'b.')
    Rresult=np.array([])
plt.title('N= '+str(N)+' , stdev= '+str(stdev))
plt.xlabel('K')
plt.ylabel('<R>')
plt.savefig("stddev=0.1, N={}.png".format(N),dpi=200)

N=1000
fig=plt.figure()
for K in range(anzK):
    Rresult=Rintegrieren(x_0,Rresult,K/float(anzK),omega,timee,dt)  
    K=K/float(anzK)
    plt.plot(K,Rresult,'b.')
    Rresult=np.array([])
plt.title('N= '+str(N)+' , stdev= '+str(stdev))
plt.xlabel('K')
plt.ylabel('<R>')
plt.savefig("stddev=0.1, N={}.png".format(N),dpi=200)

stdev=0.2

N=10
fig=plt.figure()
for K in range(anzK):
    Rresult=Rintegrieren(x_0,Rresult,K/float(anzK),omega,timee,dt)  
    K=K/float(anzK)
    plt.plot(K,Rresult,'b.')
    Rresult=np.array([])
plt.title('N= '+str(N)+' , stdev= '+str(stdev))
plt.xlabel('K')
plt.ylabel('<R>')
plt.savefig("stddev=0.2, N={}.png".format(N),dpi=200)

N=100
fig=plt.figure()
for K in range(anzK):
    Rresult=Rintegrieren(x_0,Rresult,K/float(anzK),omega,timee,dt)  
    K=K/float(anzK)
    plt.plot(K,Rresult,'b.')
    Rresult=np.array([])
plt.title('N= '+str(N)+' , stdev= '+str(stdev))
plt.xlabel('K')
plt.ylabel('<R>')
plt.savefig("stddev=0.2, N={}.png".format(N),dpi=200)

N=1000
fig=plt.figure()
for K in range(anzK):
    Rresult=Rintegrieren(x_0,Rresult,K/float(anzK),omega,timee,dt)  
    K=K/float(anzK)
    plt.plot(K,Rresult,'b.')
    Rresult=np.array([])
plt.title('N= '+str(N)+' , stdev= '+str(stdev))
plt.xlabel('K')
plt.ylabel('<R>')
plt.savefig("stddev=0.2, N={}.png".format(N),dpi=200)





#########Animation:
#result=integrieren(x_0,result,K,omega,timee,dt)
#plt.ioff()
#for j in range(int(timee/dt)):
  #  plt.scatter(sin(result[j,:]),cos(result[j,:]),c=np.array(range(N)))
  #  plt.xlim(-1.5,1.5)
  #  plt.ylim(-1.5,1.5)
  #  plt.title('t= '+str(j)+' , K= '+str(K)+' , N= '+str(N)+' , stdev= '+str(stdev))
  #  plt.savefig("./bilder/t{}.png".format(j),dpi=200)
  #  plt.close()
###animation:

########################################################
stop = time.time()
print stop-start,'\t'


    