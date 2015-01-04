import sys
import numpy as np
import matplotlib.pylab as plt


try:     driverID = int(sys.argv[1])
except:  driverID = 1

#__test__ = 'trip'
#__test__ = 'velocity'
__test__ = 'acceleration'



for tripID in range(1,201):
   fname = '../../drivers/%i/%i.csv'%(driverID,tripID)
   x,y = np.loadtxt(fname,skiprows=1,delimiter=',',unpack=True)

   #trip realization
   if  __test__ == 'trip' :
      plt.plot(x,y)

   # velocity realization
   if  __test__ == 'velocity' :
      velocity = np.sqrt( (x[1:]-x[:-1])**2 + (y[1:]-y[:-1])**2 )
      hist,bins = np.histogram(velocity, bins=40, range=[5,45], normed=True)
      plt.plot((bins[1:]+bins[:-1])/2,hist)

   # acceleration realization
   if  __test__ == 'acceleration' :
      velocityX = (x[1:]-x[:-1])
      velocityY = (y[1:]-y[:-1])
      acceleration =  np.sqrt(   (velocityX[1:]-velocityX[:-1])**2 \
                               + (velocityY[1:]-velocityY[:-1])**2 )
      hist,bins = np.histogram(acceleration, bins=40, range=[1,10], normed=True)
      plt.plot((bins[1:]+bins[:-1])/2,hist)

#if  __test__ == 'velocity' :
#   plt.ylim([0,30])
#if  __test__ == 'acceleration' :
#   plt.ylim([0,10])

plt.show()




