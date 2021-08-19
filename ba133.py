#!/usr/bin/python3

import datetime
from math import *
from printVal import printVal

# Input run date and time in CST (or CDT with correction uncommented)
rt  = datetime.datetime(2020, 2,14, 8,46) # Run time in CDT
dt  = datetime.timedelta( hours = 1 )
rt += dt # convert to CST if uncommented

ct  = datetime.datetime(2018, 4, 1,12) # Calbration time in UTC
dt  = datetime.timedelta( hours =-6 )
ct += dt # convert to CST
dt  = rt - ct
decay_time = dt.total_seconds() # in seconds

#change based on the radiation certificates
A   = 39.3e3 # in Bq
dA  =  3 # in percent (~95% C.L. or about 2 sigma)
dA /=  2 # convert to 1 sigma error

decay_fraction = exp( - decay_time * log(2)/( 1600*365.25*86400 ))
A  *= decay_fraction
dA *= A/100 # convert to absolute uncertainty


print( 'Source activity.......:', A, '+/-', dA, 'Bq' )
print( '             or.......:', printVal(A, dA, 68), 'Bq' )

dA *= dA/(A*A) # square error since that is all that will be used below

efficiency = [] # efficiency array

# ba-53.1622 lines
e   = 53.1622     # keV
a   = 2.71495     # Bq
da  = 0.0545331   # Bq
br  = 2.14        # branching ratio of transition (in %)
br /= 100         # branching ratio of transition (absolute)
a  /= br          # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a)    # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# ba-80 lines
e   = 80.9979     # keV
a   = 47.164      # Bq
da  = 0.169475    # Bq
br  = 32.9        # branching ratio of transition (in %)
br /= 100         # branching ratio of transition (absolute)
a  /= br          # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a)    # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# ba-276 lines
e   = 276.394     # keV
a   = 6.51028     # Bq
da  = 0.0634291   # Bq
br  = 7.16        # branching ratio of transition (in %)
br /= 100         # branching ratio of transition (absolute)
a  /= br          # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a)    # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# ba-302 lines
e   = 302.851     # keV
a   = 15.8114     # Bq
da  = 0.0941208   # Bq
br  = 18.34       # branching ratio of transition (in %)
br /= 100         # branching ratio of transition (absolute)
a  /= br          # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a)    # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# ba-356 lines
e   = 356.013     # keV
a   = 48.4709     # Bq
da  = 0.161065    # Bq
br  = 62.05       # branching ratio of transition (in %)
br /= 100         # branching ratio of transition (absolute)
a  /= br          # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a)    # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# ba-383 lines
e   = 383.8485    # keV
a   = 6.70065     # Bq
da  = 0.0620717   # Bq
br  = 8.94        # branching ratio of transition (in %)
br /= 100         # branching ratio of transition (absolute)
a  /= br          # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a)    # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] ) 

for eff in efficiency:
    print( eff )
print("efficiency\n",efficiency)

#save the array to the text file
import numpy as np
outputfile="ba133en_eff_error.csv"
np.savetxt(outputfile,efficiency,delimiter=",")
#storing the data in the file 
#outputfile="test.csv"
#with open(outputfile) as f:
#    for eff in efficiency:
#        for i in eff:
#            f.write(str(i))
