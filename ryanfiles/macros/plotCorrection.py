#!/usr/bin/python3

import array
from   matplotlib import pyplot
import numpy
import sys
import os

import ROOT

from   printVal   import printVal

ethresh = 60 # keV

if len(sys.argv) > 1:
    parent = sys.argv[1]

print("\nWorking for correction file of "+parent+" ...\n")
#else plot them all
#################################################
fileloc="/home/thakur/mylab/ryanfiles/multisimulation/feb18/"
f=fileloc+'correctionfeb18.dat'                                    
print("correction data file:\t",f)
#date="feb17"
data = []
file = open(f, 'r')
for line in file:
    words = line.split()
    if len(sys.argv) > 1:
        if words[0] != parent:
            continue
    data.append([
        [ words[0],        # 0: parent
          words[1] ],      # 0: isotope
        float(words[2]),   # 1: energy
        float(words[3]),   # 2: efficiency correction
        float(words[4]),   # 3: total error for a single gamma-ray (minus)
        float(words[5]),   # 4: total error for a single gamma-ray (plus)
        float(words[6]),   # 5: uncorrelated error (minus)
        float(words[7]),   # 6: uncorrelated error (plus)
        float(words[8]),   # 7: fractional correlated error (minus)
        float(words[9]) ]) # 8: fractional correlated error (plus)
for entry in reversed(range(len(data))):
    for e in range(entry):
        # If this entry's isotope and energy match a later one, then remove it.
        if data[e][0] == data[entry][0] and data[e][1] == data[entry][1]:
            data.remove(data[e])
            break

for entry in range(len(data)):
    data[entry] = [0] + data[entry][1:] # remove non-floats (isotope names)
data = numpy.array(data)

pyplot.errorbar(data[:,1], data[:,2], yerr=[data[:,5], data[:,6]], fmt='.' )
pyplot.xlabel('Energy/keV')
pyplot.ylabel('Data/simulation')
pyplot.title(parent+"(correction-feb18)")
pyplot.autoscale(enable=True)
#pyplot.xlim(0, 2500)
#pyplot.ylim(0,    2)

pol0  = ROOT.TF1('pol0','[0]',0,2500)
pol0.SetParameter(0,1)
pol1  = ROOT.TF1('pol1','[0]+[1]*x',0,2500)
pol1.SetParameters(1,0)

#file to store the correction values
#f=date+'sourceCorrection.dat'
#if os.path.exists(f):
#    print(f," exits!")
#    os.remove(f)
#    print(f," deleted!")
#else:
#    print(f," doesnot exit!")
#    #os.remove(f)
#    print(f," will be created!")
#

#mightneed to remove it if alreay presents
file = open(fileloc+'sourceCorrectionfeb18.dat', 'a')
if sum(ene > ethresh for ene in data[:,1]) > 1:
    # Fit and plot correction as a function of energy for all calibrations.
    graph = ROOT.TGraphAsymmErrors( len(data[:,1]),
                                    array.array('d', data[:,1]),
                                    array.array('d', data[:,2]),
                                    0,
                                    0,
                                    array.array('d', data[:,5]),
                                    array.array('d', data[:,6]) )
    result = graph.Fit('pol0','remqs','',60,2500)
    result.Print()
    file.write('{:6s} {:e} {:e} {:e} {:e} {:e}\n'.format( parent,
                                                          result.Parameters()[0],
                                                          -result.LowerError(0),
                                                          result.UpperError(0),
                                                          data[0][7], data[0][8] ))
    xs = numpy.linspace(0, 2500, num=2501)
    ys = []
    for x in xs:
        ys.append( pol0.Eval(x) )
    pyplot.plot(xs, ys)
elif sum(ene > ethresh for ene in data[:,1]) == 1:
    file.write('{:6s} {:e} {:e} {:e} {:e} {:e}\n'.format( parent,
                                                          data[:,2][-1],
                                                          data[:,5][-1],
                                                          data[:,6][-1],
                                                          data[0][7], data[0][8] ))
else:
    file.write('{:6s} {:e} {:e} {:e} {:e} {:e}\n'.format( parent,
                                                          -9,1,1,
                                                          data[0][7], data[0][8] ))
file.close()

pyplot.savefig(fileloc+'correctionfeb18'+parent+'.pdf', bbox_inches='tight')
