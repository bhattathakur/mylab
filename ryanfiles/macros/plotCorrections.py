#!/usr/bin/python3

import array
from   matplotlib import pyplot
import numpy
import sys
import os

import ROOT

ethresh = 60 # keV
###############################################33
fileloc="/home/thakur/mylab/ryanfiles/multisimulation/0.7-40.2-ra/"
f=fileloc+'sourceCorrection0.7-40.2-ra.dat'
print("Source correction data file:\t",f)

#check if file exists
if os.path.exists(f):
    print("file exists: ",f)
    #os.remove(f)
    #print("file removed: ",f)
else:
    print("file doesnot exist: ",f)

#print("file:\t",f)

data = []
file = open(f, 'r')
for line in file:
    print("line:\t",line)
    words = line.split()
    data.append([
        words[0],          # 0: parent
        float(words[1]),   # 1: correction
        float(words[2]),   # 2: uncorrelated error (minus)
        float(words[3]),   # 3: uncorrelated error (plus)
        float(words[4]),   # 4: fractional correlated error (minus)
        float(words[5]) ]) # 5: fractional correlated error (plus)
for entry in reversed(range(len(data))):
    for e in range(entry):
        # If this entry's isotope and energy match a later one, then remove it.
        if data[e][0] == data[entry][0]:
            data.remove(data[e])
            break

# Make isotope names nice for axis labels.
parents = []
for d in data:
    parents.append(d[0])
for p in range(len(parents)):
    parents[p] = parents[p][0].upper()+parents[p][1]+'-'+parents[p][2:]
xs = numpy.arange(0, len(parents))

for entry in range(len(data)):
    data[entry] = [0] + data[entry][1:] # remove non-floats (isotope names)
data = numpy.array(data)

c   = data[:,1]
lo  = data[:,2]
hi  = data[:,3]

# Add in source activity error.
lo2  = lo
hi2  = hi
lo2  = lo2/data[:,1] # why does /= now work here
lo2 /= data[:,1]
lo2 *= lo2
lo2 += data[:,4]*data[:,4]
lo2  = numpy.sqrt(lo2)
lo2 *= data[:,1]
hi2  = hi2/data[:,1] # why does /= now work here
hi2 *= hi2
hi2 += data[:,5]*data[:,5]
hi2  = numpy.sqrt(hi2)
hi2 *= data[:,1]

# Remove sources with lines only below threshold (at least for now).
keep = []
for d in range(len(data)):
    if data[d][1] > 0:
        keep.append(d)
c   =  c[keep]
lo  = lo[keep]
hi  = hi[keep]
lo2 = lo2[keep]
hi2 = hi2[keep]
x   = xs[keep]

pyplot.errorbar(x, c, yerr=[lo, hi], fmt='.' )
pyplot.ylabel('Data/simulation')
pyplot.xlim(xs[0]-0.5, xs[-1]+0.5)
pyplot.xticks(xs, parents)
#pyplot.ylim(0.0, 1.2)
pyplot.autoscale(enable=True,axis='y')
pyplot.title("correction-0.7-40.2-ra")

pol0  = ROOT.TF1('pol0','[0]',      xs[0]-0.5, xs[-1]+0.5)
pol0.SetParameter(0,1)
pol1  = ROOT.TF1('pol1','[0]+[1]*x',xs[0]-0.5, xs[-1]+0.5)
pol1.SetParameters(1,0)

graph = ROOT.TGraphAsymmErrors( len(x),
                                array.array('d', x),
                                array.array('d', c),
                                0,
                                0,
                                array.array('d', lo),
                                array.array('d', hi) )
pol0.SetParameter(0,0.9)
result = graph.Fit('pol0', 'remqs', '', xs[0]-1, xs[-1]+1)
ROOT.gStyle.SetOptFit(1011)
result.Print()
xs = numpy.linspace(xs[0]-1, xs[-1]+1, num=99)
ys = []
for x in xs:
    ys.append( pol0.Eval(x) )
pyplot.plot(xs, ys)

pyplot.savefig(fileloc+'correction-0.7-40.2-ra.pdf', bbox_inches='tight')
print("\n"+fileloc+'correction-0.7-40.2-ra.pdf created')
pyplot.clf()

xs = numpy.arange(0, len(parents))
x  = xs[keep]
pyplot.errorbar(x, c, yerr=[lo2, hi2], fmt='.' )
pyplot.ylabel('Data/simulation')
pyplot.xlim(xs[0]-0.5, xs[-1]+0.5)
pyplot.xticks(xs, parents)
#pyplot.ylim(0.0, 1.2) #ylim(bottom,top)
pyplot.autoscale(enable=True,axis='y')
pyplot.title("correction-correlated-0.7-40.2-ra")

graph = ROOT.TGraphAsymmErrors( len(x),
                                array.array('d',x),
                                c, 0, 0, lo2, hi2 )
pol0.SetParameter(0,0.9)
result = graph.Fit('pol0', 'remqs', '', xs[0]-1, xs[-1]+1)
result.Print()
#show the parameters in the graph
ROOT.gStyle.SetOptFit(1011)
xs = numpy.linspace(xs[0]-1, xs[-1]+1, num=99)
ys = []
for x in xs:
    ys.append( pol0.Eval(x) )
pyplot.plot(xs, ys)

pyplot.savefig(fileloc+'correctioncorrelated-0.7-40.2-ra.pdf', bbox_inches='tight')
print("\n"+fileloc+'correctioncorrelated-0.7-40.2-ra.pdf created')

