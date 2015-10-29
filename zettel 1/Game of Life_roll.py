# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:24:37 2015

@author: eric.bertok
"""

#Source: http://electronut.in/a-simple-python-matplotlib-implementation-of-conways-game-of-life
################################################################################
# conway.py
#
# Author: electronut.in
# 
# Description:
#
# A simple Python/matplotlib implementation of Conway's Game of Life.
################################################################################

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import timeit

N = 500
ON = 1
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N*N, p=[0.4, 0.6]).reshape((N,N))

def update(data):
  global grid
  # copy grid since we require 8 neighbors for calculation
  # and we go line by line 
  newGrid=np.copy(grid)
  summe=np.roll(grid,1,axis=0)+np.roll(grid,-1,axis=0)+np.roll(grid,1,axis=1)+np.roll(grid,-1,axis=1)+np.roll(np.roll(grid,1,axis=0),1,axis=1)+np.roll(np.roll(grid,1,axis=0),-1,axis=1)+np.roll(np.roll(grid,-1,axis=0),1,axis=1)+np.roll(np.roll(grid,-1,axis=0),-1,axis=1)
  newGrid[(grid==0) & (summe==3)]=1
  newGrid[(grid==1) & (summe<2)]=0
  newGrid[(grid==1) & (summe>3)]=0
    
  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()

