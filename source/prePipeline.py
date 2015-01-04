import sys
import numpy as np
import libraris as lib
import GlobalConstants

class MyApplication:

   def __init__(self):

      self.CONS = GlobalConstants.GlobalConstants()



   def run(self):

      drivers = lib.listdirs('../drivers/')[:10]
      velocityPDF = [] #np.zeros(self.CONS.VELOCITY_BINS_NUM)

      for driverID in drivers:

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
            # print hist
            velocityPDF.append(hist)

         print driverID + ' is DONE'

      velocityPDF = np.array(velocityPDF)

      bin  = (bins[1:]+bins[:-1])/2.
      mean = np.mean(velocityPDF,axis=0)
      err  = np.std(velocityPDF,axis=0)
      
      fname = './prePipelineData/velocityPDF.txt'
      np.savetxt(fname,np.array([bin,mean,err]).T,\
                 #header='v , mean , err', comments='#')
                )

      #print np.mean(velocityPDF,axis=0)
      #print np.std(velocityPDF,axis=0)
      #print np.var(velocityPDF,axis=0)

      """
      # velocity realization
      if  __test__ == 'velocity' :
         velocity = np.sqrt( (x[1:]-x[:-1])**2 + (y[1:]-y[:-1])**2 )
         hist,bins = np.histogram(velocity, bins=20,\
                                  range=[5,45], normed=False)
         pdf += hist
         pdfTot += hist

      # acceleration realization
      if  __test__ == 'acceleration' :
 
      for tripID in range(1,self.CONS.NUM_OF_TRIPS+1):

        fname = '../drivers/%i/%i.csv'%(driverID,tripID)
        x,y = np.loadtxt(fname,skiprows=1,delimiter=',',unpack=True)
      """

      print "DONE INSIDE APP"




if __name__ == "__main__":

   app = MyApplication()

   app.run()

   print "PRE PIPELINE DONE"














