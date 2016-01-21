import numpy as np
import matplotlib as mt
import scipy.integrate as int
mt.use('Agg')
import matplotlib.pyplot as plt
import time

gamma = 2 #float(sys.argv[1])/10.0

def diff(t,x):
	global gamma
	return [x[1],-gamma*x[1]+x[0]-x[0]**3]

def integrieren(dt=0.1,ausl=-5,geschw=0.5):
	r = int.ode(diff)
	r.set_integrator('dopri5')
	r.set_initial_value([ausl,geschw])
	E = 1
	while E>0: 
		x = r.integrate(r.t+dt)
		E = 0.5*x[1]**2-0.5*x[0]**2+0.25*x[0]**4
	if E==0:
		fixpoint = 0
	else:
		if x[0]>0:
			fixpoint = 1
		else:
			fixpoint = -1
	return fixpoint


maxx = 10
minx = -10
minxp = -25
maxxp = 25

genau = 10

X,Y = np.mgrid[minx:maxx+1/float(genau):1/float(genau),minxp:maxxp+1/float(genau):1/float(genau)]
A = np.zeros(((maxx-minx)*genau,(maxxp-minxp)*genau))

start = time.time()
for i in range(0,(maxx-minx)*genau):
	for j in range(0,(maxxp-minxp)*genau):
		A[i][j] = integrieren(ausl=X[i][0],geschw=Y[0][j])

		
stop = time.time()
print stop-start,'\t',gamma

plt.ioff()
#fig = figure()
plt.pcolor(X,Y,A, cmap='seismic')
#plt.colorbar()
plt.axes([minx,maxx,minxp,maxxp])
fname = "./Bilder/_tmp{}.png".format(np.int(gamma*10))
plt.savefig(fname)
#clf()
plt.close()
#plt.show()

