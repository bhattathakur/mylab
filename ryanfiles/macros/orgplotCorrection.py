#!/usr/bin/python3

import array
from   matplotlib import pyplot
import numpy
import sys
import os
import time
import math

import ROOT

from   printVal   import printVal

#chage default picture size and dpi in matplotlib
pyplot.rcParams["figure.figsize"]=[12,8]
pyplot.rcParams["figure.dpi"]=200
ethresh = 60 # keV

if len(sys.argv) > 1:
    parent = sys.argv[1]

print("\nWorking for correction file of "+parent+" ...\n")
#else plot them all
#################################################
fileloc="/home/thakur/mylab/ryanfiles/multisimulation/simdir/"
f=fileloc+'correctionsimdir.dat'                                    
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
pyplot.title(parent+"(correction-simdir)")
pyplot.autoscale(enable=True,axis='y')
#pyplot.xlim(0, 2500)
#pyplot.ylim(0.00,2.00)

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
file = open(fileloc+'sourceCorrectionsimdir.dat', 'a')
if sum(ene > ethresh for ene in data[:,1]) > 1:
    # Fit and plot correction as a function of energy for all calibrations.
    print("Fit data for :"+parent)
    print()
    time.sleep(3)
    #ROOT.gStyle.SetOptFit(1111) #didnot work
    graph = ROOT.TGraphAsymmErrors( len(data[:,1]),
                                    array.array('d', data[:,1]),
                                    array.array('d', data[:,2]),
                                    0,
                                    0,
                                    array.array('d', data[:,5]),
                                    array.array('d', data[:,6]) )
    result = graph.Fit('pol0','remqs','',60,2500)
    result.Print()
    #result.gStyle.SetOptFit(1111)#not working
    #ROOT.gPad.Update() #not working
    #fit parameters
    #https://root.cern/doc/master/classTH1.html#HFitRes
    #print("fit parameters:\n",result.Parameters())

    #get the chisquare and mean
    mean=round(result.Parameter(0),3)      #p0
    meanerr=round(result.ParError(0),3)    #p0 error
    #meanlowerr=round(result.LowerError(0)    #error
    #meanhigherr=result.LowerError(0)    #error
    chi2=round(result.Chi2(),3)            #chisquare
    #print the values
    print("p0: {} p0 error: {}\n".format(mean,meanerr))
    print("chi^2: {} \n".format(chi2))

    #putting p0 and x^2 in the pyplot
    pyplot.text(2000,1.25,r"p0: "+str(mean)+" $\pm$ "+str(meanerr),color='red')
    pyplot.text(2000,1.15,r"$\chi^{2}$: "+str(chi2),color='red')


    file.write('{:6s} {:e} {:e} {:e} {:e} {:e}\n'.format( parent,
                                                          result.Parameters()[0],
                                                          -result.LowerError(0),
                                                          result.UpperError(0),
                                                          data[0][7], data[0][8] ))
    xs = numpy.linspace(0, 2500, num=2501)
    ys = []
    for x in xs:
        ys.append( pol0.Eval(x) )
    #get the information about xs and ys
    #for i in range(len(xs)):
    #    print("xs: {}  ys: {}".format(xs[i],ys[i]))
    pyplot.plot(xs, ys)
    pyplot.xticks(numpy.arange(min(xs),max(xs)+100,100))
    pyplot.xticks(rotation=70)
    pyplot.grid(axis='both',linestyle='--',linewidth=0.5,alpha=0.5)
    #annotate in the plot
    #fig,ax=pyplot.subplots()
    #for i,txt in enumerate(xs):
       # pyplot.annotate(str(txt),(xs[i],ys[i]))

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

#attempt to get 
ax=pyplot.gca()
line=ax.lines[0]
lineval=line.get_xydata()
xdata=line.get_xdata() #xdata
ydata=line.get_ydata() #ydata

#print("xy-val",lineval)
#annotate

for i,txt in enumerate(xdata):
  pyplot.annotate(str(txt),(xdata[i],ydata[i]),fontsize=5)

#pyplot.figure(figsize=(12,8))
pyplot.savefig(fileloc+'correctionsimdir'+parent+'.pdf', bbox_inches='tight')

print("Plot are at "+fileloc+'correctionsimdir'+parent+'.pdf')

#pyplot.show()

