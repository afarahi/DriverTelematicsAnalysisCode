import sys
import numpy as np
import GlobalConstants


class driver:



   def __init__(self):

      self.CONS = GlobalConstants.GlobalConstants()



   def readAllCoordinates(self,driverID):

      xTrip = [];      yTrip = [] 

      for tripID in range(1,self.CONS.NUM_OF_TRIPS+1):

        fname = '../drivers/%s/%i.csv'%(driverID,tripID)
        x,y = np.loadtxt(fname,skiprows=1,delimiter=',',unpack=True)
        xTrip.append(x); yTrip.append(y)

      return xTrip, yTrip



   def makePDFVelocityOfDriver(self,driverID):

      velocityPDF = []

      #generating velocity pdf
      for tripID in range(1,self.CONS.NUM_OF_TRIPS):

         fname = '../drivers/%s/%i.csv'%(driverID, tripID)
         x,y = np.loadtxt(fname, skiprows=1, delimiter=',', unpack=True)
         velocity = np.sqrt( (x[1:]-x[:-1])**2 + (y[1:]-y[:-1])**2 )
         hist,bins = np.histogram(velocity,\
                          bins=self.CONS.VELOCITY_BINS_NUM,\
                          range=[self.CONS.VELOCITY_MIN,\
                                 self.CONS.VELOCITY_MAX],\
                                     normed=True)

         if np.isnan(hist[1]): continue
           
         velocityPDF.append(hist)

      print driverID + ' velocity PDF is created.'

      velocityPDF = np.array(velocityPDF)

      bin  = (bins[1:]+bins[:-1])/2.
      mean = np.mean(velocityPDF,axis=0)
      err  = np.std(velocityPDF,axis=0)
      
      return bin, mean, err



   def categoryOfAcceleration(self,driverID):

      pdf = np.zeros(self.CONS.ACCELERATION_BINS_NUM)
 
      #generating velocity pdf
      for tripID in range(1,self.CONS.NUM_OF_TRIPS):

         fname = '../drivers/%s/%i.csv'%(driverID, tripID)
         x,y = np.loadtxt(fname, skiprows=1, delimiter=',', unpack=True)
         velocityX = (x[1:]-x[:-1]); velocityY = (y[1:]-y[:-1])
         acceleration =  np.sqrt(   (velocityX[1:]-velocityX[:-1])**2 \
                                  + (velocityY[1:]-velocityY[:-1])**2 )
      
         hist,bins = np.histogram(acceleration,\
                          bins=self.CONS.ACCELERATION_BINS_NUM,\
                          range=[self.CONS.ACCELERATION_MIN,\
                                 self.CONS.ACCELERATION_MAX],\
                                     normed=True)

         if np.isnan(hist[1]): continue

         pdf += hist
           
      print driverID + ' acceleration catagory is determined.'

      if ( sum(pdf[8:12])-sum(pdf[12:16]) < 0 ):
         return 1
      else:
         return 2










