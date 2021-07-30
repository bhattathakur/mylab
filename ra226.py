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

A   = 29.7e3 # in Bq
dA  =  3 # in percent (~95% C.L. or about 2 sigma)
dA /=  2 # convert to 1 sigma error

decay_fraction = exp( - decay_time * log(2)/( 1600*365.25*86400 ))
A  *= decay_fraction
dA *= A/100 # convert to absolute uncertainty


print( 'Source activity.......:', A, '+/-', dA, 'Bq' )
print( '             or.......:', printVal(A, dA, 68), 'Bq' )

dA *= dA/(A*A) # square error since that is all that will be used below

efficiency = [] # efficiency array

# Ra-226 lines
e   = 186.211    # keV
a   = 3.35879    # Bq
da  = 0.0875405# Bq
br  = 3.64 # branching ratio of transition (in %)
br /= 100    # branching ratio of transition (absolute)
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

at218br  = 0.02/100

# Pb-214 lines
pb214br = 99.980/100
e   = 241.9950 # keV
a   =   5.96801   # Bq
da  =   0.0875405# Bq
br  =   7.251 # branching ratio of transition from Pb-214 (in %)
br /= 100
br *= pb214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# Pb-214 lines
pb214br = 99.980/100
e   = 295.224# keV
a   =   13.3358   # Bq
da  =   0.11436# Bq
br  =   18.42 # branching ratio of transition from Pb-214 (in %)
br /= 100
br *= pb214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# Pb-214 lines
pb214br = 99.980/100
e   = 351.932# keV
a   = 23.7357# Bq
da  = 0.146055# Bq
br  = 35.60# branching ratio of transition from Pb-214 (in %)
br /= 100
br *= pb214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# Total Bi-214 branching ratio (from two routes)
bi214br = []
bi214br.append( at218br )
bi214br[-1] *= 99.90/100
bi214br.append( pb214br )
bi214br[-1] *= 99.979/100
bi214br = sum( bi214br )

# Bi-214 lines:
e   = 609.320 # keV
a   =   21.4852# Bq
da  =   0.136137 # Bq
br  =  45.49  # branching ratio of transition from Bi-214 (in %)
br /= 100
br *= bi214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# Bi-214 lines:
e   = 1120.294# keV
a   =   5.0864# Bq
da  =   0.0661253# Bq
br  =  14.92# branching ratio of transition from Bi-214 (in %)
br /= 100
br *= bi214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# Bi-214 lines:
e   =1238.122# keV
a   =1.83993# Bq
da  =0.0409898# Bq
br  =5.834# branching ratio of transition from Bi-214 (in %)
br /= 100
br *= bi214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# Bi-214 lines:
e   = 1764.491# keV
a   = 3.84105# Bq
da  = 0.0578668# Bq
br  = 15.30  # branching ratio of transition from Bi-214 (in %)
br /= 100
br *= bi214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# Bi-214 lines:
e   = 2204.059# keV
a   = 1.09519# Bq
da  = 0.0305912# Bq
br  = 4.924# branching ratio of transition from Bi-214 (in %)
br /= 100
br *= bi214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )

# Bi-214 lines:
e   =2447.70# keV
a   =0.323963# Bq
da  =0.0166171# Bq
br  =1.548# branching ratio of transition from Bi-214 (in %)
br /= 100
br *= bi214br # branching ratio of transition from Ra-226
a  /= br # activity of Ra-226 implied by observed activity
da /= br
da *= da/(a*a) # square error
eff = a/A
efficiency.append( [e, eff, eff*sqrt(da + dA)] )
for eff in efficiency:
    print( eff )
print("efficiency\n",efficiency)

#save the array to the text file
import numpy as np
outputfile="en_eff_error.csv"
np.savetxt(outputfile,efficiency,delimiter=",")
#storing the data in the file 
#outputfile="test.csv"
#with open(outputfile) as f:
#    for eff in efficiency:
#        for i in eff:
#            f.write(str(i))
