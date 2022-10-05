#!/usr/bin/python3
'''
This program produces the sim.dat file based on the mac file (used in simulation), gdf file (used to fit simulation data file) and original gdf file
'''

import math
import re
import sys

from printVal import printVal
from readGDF  import readGDF
from ra226BR  import *

#Example input:
#./sim.py co60 ~/gesim/sources/door/co60.mac co60sim.gdf ~/ge4/gdf/co60/co60.gdf

parent   = sys.argv[1]
macFile  = sys.argv[2]
gdfFile  = sys.argv[3] #gdf file for fitting the simulated data
gdfFile0 = sys.argv[4] #original gdf file
no_of_files=N_files

print("parent:\t",parent)
print("macFile:\t",macFile)
print("gdfFile:\t",gdfFile)
print("gdfFile0:\t",gdfFile0)
print("Num of files:\t",no_of_files)

# Get number of simulated events from Geant4 mac file.
file = open(macFile, "r")
for line in file:
    # This should find the last line that begins with (not commented out) beamOn.
    if re.search('^/run/beamOn', line):
        N = int( line.split()[1] )
        print("N in a mac file:   {}\n".format(N))
        #changing N for given files
        print("Number of simulation files: {}\n".format(no_of_files))
        N=no_of_files*N
        print("N in a simulation: {}\n".format(N))

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
[livetime, data]  = readGDF( gdfFile, isotopes)
# Need to get B.R. error from original gdf file. gdfit sets it to sqrt(2).
[dummy,    data2] = readGDF( gdfFile0, isotopes )
for d in data:
    for d2 in data2:
        if d2[0] == d[0]:
            d[2] = d2[2]
            break
    if d[2] == 0:
        print( 'Warning:',d[0],'keV branching ratio has no error.' )

print("OPEANING and READING sim.dat")
file = open('sim.dat','a')
for d in data:
    if d[4] > 0: # gamma line was fit
        if d[3]/d[4] >= 3: # 3 sigma measurement
            eff = d[3]/d[1]*livetime/N
            lo  = d[4]/d[1]*livetime/N/eff
            lo  = math.sqrt( lo*lo + d[2]*d[2]/(d[1]*d[1]) )
            lo *= eff
            hi  = lo
            print( 'Number simulated......: ', N )
            print( "Simulated efficiency..:", eff, '+', hi, '/-', lo )
            print( "                  or..:", printVal(eff, (lo+hi/2)) )

            file.write( '{:6s} {:6s} {:.4f} {:e} {:e} {:e} {:d} {:e} {:e} {:e} {:e} {:e}\n'.format(parent,
                                                                                             d[-1], d[0],
                                                                                             eff, hi, lo,
                                                                                             N, livetime,
                                                                                             d[1], d[2], d[3], d[4]) )
            print( 'parent->{:6s}\td[-1]-> {:6s}\td[0]-> {:.4f}\teff-> {:e}\thi-> {:e}\tlow-> {:e}\tN-> {:d}\tlivetime-> {:e}\td[1]-> {:e}\td[2]-> {:e}\td[3]-> {:e}\td[4]->{:e}\n'.format(parent,
                                                                                             d[-1], d[0],
                                                                                             eff, hi, lo,
                                                                                             N, livetime,
                                                                                             d[1], d[2], d[3], d[4]) )

file.close()
