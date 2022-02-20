#This macro is intended to combine multiple data files into a single one

import pandas as pd
import numpy as np
import time

#read files
file_count=20 #file count change

root='/home/thakur/mylab/ryanfiles/multisimulation/batch_gesim/' #location to save final data file

print("Resulting data file is saved at: ",root)

chn_no=16384
files=['am241','ba133','co60','cs137','eu152','na22','pb210','ra226']
for i in files:
    print(20*'=');print("Working for: "+i);print(20*'=')
    base=i
    suff="sim.dat"

    f=base+"0"+suff
    print("file:\t",f)
    print("Loading file:\t",f)
    x0,y0=np.loadtxt(f,unpack=True)
    y0=y0.reshape(chn_no,1)
    x0=x0.reshape(chn_no,1)
    print("y0\n",y0)
    time.sleep(0.5)

    for i in range(1,file_count):
        f=base+str(i)+suff
        print("Loading file:\t",f)
        time.sleep(0.5)

        #load the file
        x,y=np.loadtxt(f,unpack=True)
        print("y\n",y)
        #print("shape\t",f1.shape)
        print("Horizontally stacked...\n")
        y=y.reshape(chn_no,1)
        print("y\n",y)

        y0=np.hstack((y0,y))
        print("base\n",y0)


    #summing the columns along axis=1
    s=np.sum(y0,axis=1)
    print("sum\n:",s)
    s=s.reshape(chn_no,1)
    print("sum\n:",s)
    #print("Base:\n",base.shape)
    #chn and sum of columns
    f=np.hstack((x0,s))
    print("f\n",f)

    #save the array into a file
    savefile=root+base+suff
    print("save location:\t",savefile)

    np.savetxt(savefile,f,fmt="%i")

    print("File saved as:\t",base+suff)
print("Done!")
