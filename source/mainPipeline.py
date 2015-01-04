import sys
import numpy as np
import libraries as lib

class MyApplication:

   def __init__(self):

      import driver as dr
      import GlobalConstants
      self.CONS = GlobalConstants.GlobalConstants()
      self.driver = dr.driver() 


   def run(self,driverID):

      _, meanV, errV = self.driver.makePDFVelocityOfDriver(driverID)

      for tripID in range(1,self.CONS.NUM_OF_TRIPS+1):

         fname = '../drivers/%s/%i.csv'%(driverID,tripID)
         x,y = np.loadtxt(fname,skiprows=1,delimiter=',',unpack=True)
         vx, vy = lib.calVelocity(x,y)
         ax, ay = lib.calAcceleration(vx,vy)





      print "DONE INSIDE APP"




if __name__ == "__main__":

   app = MyApplication()

   #
   driverID = '10'
   app.run(driverID)

   print "DONE MIAN"














