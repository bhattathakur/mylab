#!/usr/bin/python3

from math       import *
from matplotlib import pyplot
import numpy
import random
import scipy.optimize

root2 = sqrt(2)
def gaussian(x, A, mu, sigma):
    #    return A * 1/(sigma*sqrt(2*pi)) * numpy.exp(-0.5*( (x - mu)/sigma )**2)
    erf  = scipy.special.erf( (x+width-mu)/(root2*sigma) )
    erf -= scipy.special.erf( (x      -mu)/(root2*sigma) )
    return 0.5 * A * erf

def getdA(A, dA, hl, dhl, dhlp, start, end):
    #  A.....: source activity
    # dA.....: 1 sigma uncertainty on source activity
    #  hl....: halflife in seconds
    # dhl....: error in halflife in seconds
    # dhlp...: +0.25 days if halflife is given in years
    global width
    nbins  = 40
    throws =  1e6

    a = A * hl/log(2) * ( exp(-start*log(2)/hl) -  exp(-end*log(2)/hl) ) / (end - start)
    
    dist = []
    min =  inf
    max = -inf
    while len(dist) < throws:
        da  = random.gauss(A, dA) #(mu,sigma)
        dt  = random.gauss(hl, dhl)
        dt += dhlp*(random.random() < 0.5)
        da *= dt/log(2) * ( exp(-start*log(2)/dt) -  exp(-end*log(2)/dt) ) / (end - start)
        da  = a - da
        if da < min:
            min = da
        elif da > max:
            max = da
        dist.append(da)

    bins   = numpy.linspace(min, max, nbins)
    width  = max - min
    width /= nbins

    [weights, bins, patches] = pyplot.hist(dist, bins=bins)

    #centers = []
    #for bin in range(1, len(bins)):
    #    centers.append( (bins[bin-1] + bins[bin])/2 )

    init  = [
        throws*(max-min)/nbins,
        (max + min)/2,
        (max - min)/2
    ]
    popt, pcov = scipy.optimize.curve_fit( gaussian,
                                           xdata=bins[:-1],
                                           #fitting integral of gaus
                                           #xdata=centers,
                                           ydata=weights,
                                           p0=init )
    x  = numpy.linspace(min, max, 100000)
    pyplot.plot(x, gaussian(x-width/2, *popt), color='darkorange', linewidth=2.5)
    pyplot.xlim(min, max)

    #pyplot.yscale('log', nonposy='clip')
    pyplot.savefig('dist.pdf', bbox_inches='tight')
    pyplot.cla()
    pyplot.clf()
    pyplot.close()

    return [ popt[1] - popt[2], popt[1] + popt[2] ]
