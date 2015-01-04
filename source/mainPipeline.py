import sys
import numpy as np
import libraries as lib
from solver import solve

class MyApplication:

   def __init__(self):

      import driver as dr
      import GlobalConstants
      self.CONS = GlobalConstants.GlobalConstants()
      self.driver = dr.driver() 


   def run(self,driverID):

      counterP = 0; counterN = 0

      fnameSave = '../outputData/%s.csv'%driverID
      f = open(fnameSave,'w')

      #_, meanV, errV = self.driver.makePDFVelocityOfDriver(driverID)
      accCat = self.driver.categoryOfAcceleration(driverID)
      print accCat

      for tripID in range(1,self.CONS.NUM_OF_TRIPS+1):

         fname = '../drivers/%s/%i.csv'%(driverID,tripID)

         x,   y = np.loadtxt(fname,skiprows=1,delimiter=',',unpack=True)
         vx, vy = lib.calVelocity(x,y)
         ax, ay = lib.calAcceleration(vx,vy)
         accCatTrip = lib.calAccelerationCatagory(ax,ay)
         p = solve(accCat,accCatTrip)

         f.write('%s_%i,%0.2f\n'%(driverID,tripID,p))

         if ( accCatTrip == accCat ):           counterP += 1
         else:                                  counterN += 1

      f.close()

      print counterP, counterN, float(counterP)/200.0

      print "DONE INSIDE APP"




if __name__ == "__main__":

   app = MyApplication()

   drivers = lib.listdirs('../drivers/')
   for driverID in drivers:  app.run(driverID)

   print "DONE MIAN"














