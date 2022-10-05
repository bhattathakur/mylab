#!/usr/bin/python3

import datetime
import math
import sys

from printVal      import printVal
from getA          import getA
from readGDF       import readGDF
from getRatioError import getRatioError
from ra226BR       import *

fmt="{}\t\t{}"
geiv_data_file="final_door_data.dat" #final combined data is saved in this file

def getRunTimes(datFile):
    """
    reads the 3rd and 4th line of the data file which is obtained from Chn files and returns start and end time
    """
    print(f"Reading the file: {datFile}")
    file = open(datFile, 'r')
    lines = file.readlines()
    #readline reads a whole file in a go and store in the form of list of strings.
    start =           int(lines[2].split()[-2])
    end   = start + float(lines[3].split()[-2])
    return [start, end]

"""
The form of lines which getRunTimes reads:
    Run started....................:  Fri Feb 14 10:22:43 2020
       in time zone.................:  CST
       in time since epoch..........:  1581697363 s
     Run  time......................:         251.90 s
     Live time......................:         251.52 s
     Number of data channels........:       16384

"""
#epoch->Jan 01,1970 (also called unix time, posix time)


#Example input:
#./data.py co60 ~/ge4/ana/2020/effcal/02-14/door/dat/co60.dat co60.gdf ~/ge4/gdf/co60/co60.gdf

parent   = sys.argv[1]
datFile  = sys.argv[2] #data file obtained for the corresponding Chn file->gives start and end time
gdfFile  = sys.argv[3] #gdf file which best fits the data file
gdfFile0 = sys.argv[4] #original gdf file 

[start, end] = getRunTimes(datFile) #start,end time

[A, dA, minus, plus] = getA(parent,
                              datetime.datetime.fromtimestamp(start, datetime.timezone.utc),
                              datetime.datetime.fromtimestamp(end,   datetime.timezone.utc) )

#datetime.fromtimestamp(ts) converts "seconds since the epoch" to a naive datetime object that represents local time. tzinfo is always None in this case.
#getA is getting activities based on the source certificates and start and end time
isotopes = [[ parent, 1 ]]
if   parent == 'eu152' or parent == 'Eu152' or parent == 'Eu-152':
    isotopes = [
        ['eu152b', 27.92e-2, 13e-4 ],
        ['eu152e', 72.08e-2, 13e-4 ]
    ]
elif parent == 'ra226' or parent == 'Ra226' or parent == 'Ra-226':
    isotopes = [
        [ 'ra226', 1 ],
        [ 'pb214', pb214br ],
        [ 'bi214', bi214br ],
        [ 'pb210', pb210br ]
    ]

# Read all gamma-ray data for this source.
[livetime, data]  = readGDF( gdfFile,  isotopes )
# Need to get B.R. error from original gdf file. gdfit sets it to sqrt(2).
[livetime, data2] = readGDF( gdfFile0, isotopes )
for d in data:
    for d2 in data2:
        if d2[0] == d[0]:
            d[2] = d2[2]
            break
    if d[2] == 0:
        print( 'Warning:',d[0],'keV branching ratio has no error.' )

file = open(geiv_data_file,'a')
for d in data:
    if d[4] > 0: # gamma line was fit
        if d[3]/d[4] >= 3: # number of sigma measurement
            print( '' )
            # Get observed source activity implied by activity of this transition and its B.R.
            print( 'Observed activity.....:', d[0], d[3]/d[1], d[4]/d[1], 'Bq' )# fit rate/B.R. of gamma
            print( '               or.....:', d[0], printVal(d[3]/d[1], d[4]/d[1]), 'Bq' )

            # Divide the observed activity by the source activity to get efficiency.
            eff = d[3]/d[1]/A
            lo  = d[4]/d[3] * eff
            hi  = lo
            #[lo, hi] = getRatioError(d[3]/d[1], d[4]/d[1], d[4]/d[1], A, 0, 0)
            #lo = eff - lo
            #hi = hi - eff
            # Print observed efficiency (observed activity/source activity).
            print( 'Observed efficiency...:', eff, '+', hi, '/-', lo    )
            print( '                 or...:', printVal(eff, (lo+hi)/2 ) )

            file.write( '{:6s} {:6s} {:.4f} {:e} {:e} {:e} {:e} {:e} {:e} {:e} {:e} {:e} {:e} {:e}\n'.format(parent,
                                                                                                             d[-1], d[0],
                                                                                                             eff, lo, hi,
                                                                                                             A, dA, minus, plus,
                                                                                                             d[1], d[2], d[3], d[4]) )
            #print("parent\t d[-1]d[0]\teff\tlo\thi\tA\tdA\tminus\tplus\n")
            print("DATA\n")
            print( 'parent->{:6s}\td[-1]-> {:6s}\td[0]-> {:.4f}\teff-> {:e}\tlo-> {:e}\thi-> {:e}\tA-> {:e}\tdA-> {:e}\tminus-> {:e}\tplus-> {:e}\t d[1]->{:e}\td[2]-> {:e}\td[3]-> {:e}\td[4]-> {:e}\n'.format(parent,
                                                                                                             d[-1], d[0],
                                                                                                             eff, lo, hi,
                                                                                                             A, dA, minus, plus,
                                                                                                             d[1], d[2], d[3], d[4]) )


file.close()
