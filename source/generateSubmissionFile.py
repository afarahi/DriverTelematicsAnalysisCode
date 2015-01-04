import numpy as np
import libraries as lib

fnameSave = '../submission/submission.csv'

files = lib.listfiles('../outputData/')
files.sort()

f = open(fnameSave,'w')
f.write('driver_trip,prob\n')

for iFile in files:

  fname = '../outputData/%s'%iFile
  #lines = np.loadtxt(fname, dtype='str')
  contentFile = open(fname, 'r')
  content = contentFile.read() 
  f.write(content)
 
f.close()

