import numpy as np
import numpy.random as rnd
import scipy as sp
import matplotlib as mt
import scipy.integrate as int
#mt.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import *
import sys
import time
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

tau=30
d=3

def roess(t,x):
	return np.array([-x[1]-x[2],x[0]+0.1*x[1],0.1+x[2]*(x[0]-14)])
 
def correlation(x,N,kmax=400,plot=True):
	x_mean = np.mean(x,axis=0)
	x_vari = np.var(x,axis=0)
	
	c = np.zeros((kmax,3))
	for k in range(kmax):
		c[k] = (1.0/(x_vari*(N-k)))*np.sum((x[0:N-k]-x_mean)*(x[k:N]-x_mean),axis=0)
	if plot:        
         plt.plot(c[:,0],label='x')
         plt.plot(c[:,1],label='y')
         plt.plot(c[:,2],label='z')
         plt.legend()
         fname = "./bilder/correlation.png"
         plt.savefig(fname,dpi=200)
		
#plt.show()
plt.close()
		

def integrieren(N=1e5,dt=0.01,plot=True):
	r = int.ode(roess)
	r.set_integrator('dopri5')
	start = rnd.rand(3)*0.2
	r.set_initial_value(start)
	
	ergeb = []
	ergeb.append(start)
	while r.t/dt < N:
		ergeb.append(r.integrate(r.t+dt))
	ergeb = np.array(ergeb)

	if plot:
		fig = figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot(ergeb[:,0],ergeb[:,1],ergeb[:,2],'r-')
		fname = "./bilder/realsystem.png"
		plt.savefig(fname,dpi=500)
		plt.close()
		#plt.show()
	return ergeb
 
def reconstruct(N=1e5,plot=True):
	taux	= 150
	tauy	= taux
	tauz	= 50
	
	ergeb	= integrieren(N=N)
	series_x	= ergeb[:,0]
	series_y	= ergeb[:,1]
	series_z	= ergeb[:,2]

	correlation(ergeb,N)	
	reconz = []
	for i in range(tauz*d,len(series_z)):
		reconz.append([series_z[i],series_z[i-tauz],series_z[i-2*tauz]])
	reconz = np.array(reconz)

	recony = []
	for i in range(tauy*d,len(series_y)):
		recony.append([series_y[i],series_y[i-tauy],series_y[i-2*tauy]])
	recony = np.array(recony)

	reconx = []
	for i in range(tauz*d,len(series_x)):
		reconx.append([series_x[i],series_x[i-taux],series_x[i-2*taux]])
	reconx = np.array(reconx)
	
	if plot:
		fig = figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot(reconz[:,0],reconz[:,1],reconz[:,2],'r-')
		plt.title("Z-Recon Tau={}".format(tauz))
		fname = "./bilder/reconstruction_z{}.png".format(np.int(tauz))
		plt.savefig(fname, dpi=500)
		plt.show()
		#plt.close()
start=time.time()
reconstruct()
stop = time.time()
print stop-start,'\t'