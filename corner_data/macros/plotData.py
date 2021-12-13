#!/usr/bin/python3

import array
from   matplotlib import pyplot
import numpy
import sys

import ROOT

from   printVal   import printVal

parent = sys.argv[1]
print("working for data for "+parent+" ...")
#./plotData.py co60
# Read all entries from data.dat,
# then remove earlier superseeded entries.
data = []

#this lines (20-26)are only for pb ... comment if doing all at the same time 
#pbfile="pb210"
#pb210-1.5in.dat
#pb210-1in.dat
#pb210-2.5in.dat
#pb210.dat
#pb210-outer.dat
#file = open(pbfile+".dat", 'r') #for multiple pb-210 files

#file = open('data.dat', 'r')
test='pb210-outer'
data_file=test+".dat"
file = open(data_file,'r')

for line in file:
    words = line.split()
    if words[0] != parent:
        continue
    data.append([
        [ words[0],         # 0: parent
          words[1] ],       # 0: isotope
        float(words[ 2]),   # 1: energy
        float(words[ 3]),   # 2: efficiency
        float(words[ 4]),   # 3: uncorrelated error (minus)
        float(words[ 5]),   # 4: uncorrelated error (plus)
        float(words[ 8]),   # 5: total activity error (minus)
        float(words[ 9]) ]) # 6: total activity error (plus)
for entry in reversed(range(len(data))):
    for e in range(entry):
        # If this entry's isotope and energy match a later one, then remove it.
        if data[e][0] == data[entry][0] and data[e][1] == data[entry][1]:
            data.remove(data[e])
            break

# Separate the different daughter isotopes.
iso = [[]]
for d in data:
    if len(iso[0]) == 0:
        iso[0].append(d)
        continue
    for t in iso:
        if t[0][0][1] == d[0][1]:
            t.append(d)
            break
    else:
        iso.append([])
        iso[-1].append(d)

isotopes = [] # names of daughter isotopes
for i in iso:
    isotopes.append(i[0][0][1])

# Plot, separately, each isotope of this parent.
for i in range(len(iso)):
    for entry in range(len(iso[i])):
        iso[i][entry] = [0] + iso[i][entry][1:] # remove non-floats (isotope names)
    data = numpy.array(iso[i])
    pyplot.errorbar(data[:,1], 100*data[:,2], yerr=[100*data[:,3], 100*data[:,4]], fmt='.' )

pyplot.xlabel('Energy/keV')
pyplot.ylabel('Efficiency/%')
pyplot.xlim(0, 2500)
pyplot.ylim(0,    1)
#pyplot.title(parent+"(data)")
pyplot.title(test+"(data)")

#pyplot.savefig('data'+parent+'.pdf', bbox_inches='tight')
pyplot.savefig(test+'.pdf', bbox_inches='tight')
#pyplot.savefig('data'+pbfile+'.pdf', bbox_inches='tight')
