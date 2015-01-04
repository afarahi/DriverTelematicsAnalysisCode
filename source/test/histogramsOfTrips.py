import sys
import numpy as np
import matplotlib.pylab as plt
import os


def listdirs(folder):
    return [ d for d in os.listdir(folder) if\
             os.path.isdir(os.path.join(folder, d)) ]

__test__ = 'velocity'
#__test__ = 'acceleration'

drivers = listdirs('../../drivers/')[:]

pdfTot = np.zeros(20)
for driverID in drivers:
   pdf = np.zeros(20)

   for tripID in range(1,201):
      fname = '../../drivers/%s/%i.csv'%(driverID,tripID)
      x,y = np.loadtxt(fname,skiprows=1,delimiter=',',unpack=True)
  
      # velocity realization
      if  __test__ == 'velocity' :
         velocity = np.sqrt( (x[1:]-x[:-1])**2 + (y[1:]-y[:-1])**2 )
         hist,bins = np.histogram(velocity, bins=20,\
                                  range=[5,45], normed=False)
         pdf += hist
         pdfTot += hist

      # acceleration realization
      if  __test__ == 'acceleration' :
         velocityX = (x[1:]-x[:-1])
         velocityY = (y[1:]-y[:-1])
         acceleration =  np.sqrt(   (velocityX[1:]-velocityX[:-1])**2 \
                                  + (velocityY[1:]-velocityY[:-1])**2 )
         hist,bins = np.histogram(acceleration, bins=40, \
                                  range=[1,5], normed=False)
         pdf += hist
         pdfTot += hist


   if  __test__ == 'velocity' :
      plt.plot((bins[1:]+bins[:-1])/2,pdf/sum(pdf),\
                    'k',linewidth=0.5,alpha=0.2)

   if  __test__ == 'acceleration' :
      if ( sum(pdf[8:12])-sum(pdf[12:16]) < 0 ):
         plt.plot((bins[1:]+bins[:-1])/2,pdf/sum(pdf),\
                    'k',linewidth=0.5,alpha=0.2)
      else:
         plt.plot((bins[1:]+bins[:-1])/2,pdf/sum(pdf),\
                    'r',linewidth=0.5,alpha=0.5)

#plt.plot((bins[1:]+bins[:-1])/2,pdfTot/sum(pdfTot),'y',linewidth=5,alpha=0.5)

#if  __test__ == 'velocity' :
#   plt.ylim([0,30])
#if  __test__ == 'acceleration' :
#   plt.ylim([0,10])

plt.show()




