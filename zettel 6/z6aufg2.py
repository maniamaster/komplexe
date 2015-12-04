# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:18:28 2015

@author: eric.bertok
"""

import scipy.integrate as sp
import matplotlib.pyplot as plt
import numpy as np
import time
import math

##parameters:
b=3
x0=0.2

##functions:
def bern(b,x):
    return (b*x)%1
    


start=time.time()
#####################
result=np.empty(10000000)
result[0]=x0
for i in range(1,10000000):
    result[i]=bern(b,result[i-1])

fig=plt.figure()
plt.hist(result,100,histtype='step',normed='true')
plt.xlabel('x')
plt.ylabel('#')
plt.show()
#####################
stop=time.time()
print stop-start