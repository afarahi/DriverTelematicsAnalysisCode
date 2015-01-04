import os

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

