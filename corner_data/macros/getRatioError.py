#!/usr/bin/python3

from   math       import *
from   matplotlib import pyplot
import numpy
import random
import scipy.optimize

root2 = sqrt(2)
def gaussian(x, A, mu, sigma):
    erf  = scipy.special.erf( (x+width-mu)/(root2*sigma) )
    erf -= scipy.special.erf( (x      -mu)/(root2*sigma) )
    return 0.5 * A * erf
def getRatioError(num, num_minus, num_plus, denom, denom_minus, denom_plus):
    global width
    nbins  = 60
    throws =  1e6
    dist   = []
    min    =  inf
    max    = -inf
    while len(dist) < throws:
        r     =  abs( random.gauss(0, num_plus)  )
        if random.random() < 0.5:
            r = -abs( random.gauss(0, num_minus) )
        s     =  abs( random.gauss(0, denom_plus)  )
        if random.random() < 0.5:
            s = -abs( random.gauss(0, denom_minus) )
        ratio = (num + r)/(denom + s)
        if   ratio < min:
            min = ratio
        elif ratio > max:
            max = ratio
        dist.append( ratio )

    bins   = numpy.linspace(min, max, nbins)
    width  = max - min
    width /= nbins

    [weights, bins, patches] = pyplot.hist(dist, bins=bins)

    init  = [
        throws*(max-min)/nbins,
        (max + min)/2,
        (max - min)/2
    ]

    popt, pcov = scipy.optimize.curve_fit( gaussian,
                                           xdata=bins[:-1],
                                           ydata=weights,
                                           p0=init )
    x  = numpy.linspace(min, max, 100000)
    pyplot.plot(x, gaussian(x-width/2, *popt), color='darkorange', linewidth=2.5)
    pyplot.xlim(min, max)
    pyplot.ylim(0, throws/10)

    pyplot.savefig('dist.pdf', bbox_inches='tight')
    pyplot.cla()
    pyplot.clf()
    pyplot.close()

    return [ popt[1] - popt[2], popt[1] + popt[2] ]
