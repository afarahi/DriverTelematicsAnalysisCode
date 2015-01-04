import os
import numpy as np
import GlobalConstants as const
CONS = const.GlobalConstants()

def listdirs(folder):
   return [ d for d in os.listdir(folder) if\
           os.path.isdir(os.path.join(folder, d)) ]

def calVelocity(x,y):
   vx = x[1:]-x[:-1]
   vy = y[1:]-y[:-1]
   return vx, vy

def calAcceleration(vx,vy):
   ax = vx[1:]-vx[:-1]
   ay = vy[1:]-vy[:-1]
   return ax, ay

def calAccelerationCatagory(ax,ay):
   acceleration =  np.sqrt( ax**2 + ay**2 )
      
   hist,bins = np.histogram(acceleration,\
                  bins=CONS.ACCELERATION_BINS_NUM,\
                  range=[CONS.ACCELERATION_MIN,\
                         CONS.ACCELERATION_MAX],\
                            normed=True)

   if np.isnan(hist[1]): return 0

   if ( sum(hist[8:12])-sum(hist[12:16]) < 0 ):
      return 1
   else:
      return 2

