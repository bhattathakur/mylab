#!/usr/bin/python

import sys
from math import *
from fcGausLimits import fcGausLimits

def getErrorPrecision(dx):
    precision = 0
    if dx < 4:
        # Use precision to round
        log10dx = log10(dx)
        dxpower = int(log10dx)
        ms = int( dx/pow( 10, dxpower-1))
        precision = -dxpower + 1
        if ms < 4:
            precision += 1
    else:
        # Use precision to round
        log10dx = log10(dx)
        dxpower = int(log10dx)
        ms = int( dx/pow( 10, dxpower))
        precision = -dxpower
        if ms < 4:
            precision += 1
    return precision

#change dx to x
def getSignificant(dx, precision=0):
    if precision < 0:
        print( 'Warning:: not tested for values greater than 1 that are not more than 3 sigma' )
        precision = 0
    elif dx != 0:
        # If dx < 0 all .5s will be rounded down. This is the opposite of the case when
        # dx > 0 and the opposite of the desired result...but this result is bad either way.
        sign    = int(dx>0) - int(dx<0)
        dx     *= sign
        log10dx = log10(dx)
        dxpower = int(log10dx)
        if dx < 1: dxpower = dxpower - 1
        if dxpower > -precision: dxpower = -precision
        ms  = int( dx/pow( 10, dxpower))
        dx  = int( dx/pow( 10, dxpower - 1*(ms<4)) + 0.5 ) * pow( 10, dxpower - 1*(ms<4))
        dx *= sign
    s = '{:.'+str(precision)+'f}'
    s = s.format(dx)
    return s

def getRounded(x, precision=0):
    x = int( x/pow(10,-precision) + 0.5 )
    x = x * pow(10,-precision)
    s = '{:.0f}'
    s = s.format(x)
    return s

def printVal(x, dx, cl=90, systematic=0, debug=False):
    dx_m  = dx
    dx_p  = dx
    sigma = x/dx

    if debug:
        print( 'DEBUG:',x,'+/-',dx,'(',sigma,'sigma )' )

    # sigma is calculated before adding the systematic so this should be fine:
    dx *= 1 + systematic
    if x > 0:
        dx = sqrt(dx*dx + systematic*x * systematic*x)
    precision = getErrorPrecision(dx)
    if debug:
        print( 'DEBUG: error precision is', precision )
    if precision < 0:
        s  = getRounded(  x, precision )
        s += ' +/- '
        s += getRounded( dx, precision )
        s += '\t'
    else:
        s  = getSignificant(  x, precision )
        s += ' +/- '
        s += getSignificant( dx, precision )
        s += '\t'
    
    lim = ''
    if sigma >= -3 and sigma <= 3.1:
        [ll, ul] = fcGausLimits( sigma, 68 )
        # dx_m should be 0 if sigma < 0.5 ish
        dx_m = 0
        if x > 0:
            dx_m =     x - ll*dx
        dx_p = ul*dx - x # if x is negative this frigs up

        if ll == 0:
            lim = x + dx_p
            precision = getErrorPrecision(lim)
            lim = getSignificant(lim, precision)
            s += '< '
            s += lim
            s += ' ('
            s += str(68.27)
            s += '% C.L.)'
            s += '\t'
            
        else:
            precision = getErrorPrecision(dx_m)
            dx_m_str = getSignificant( dx_m, precision )
            dx_p_str = getSignificant( dx_p, precision )
    
            if dx_m_str != dx_p_str:
                # then print asymmetric errors
                s +=  getSignificant(  x,   precision )
                s += ' +'
                s += dx_p_str
                s += '/-'
                s += dx_m_str
                s += '\t'

        if sigma < 1.9:# at this point 1sigma C.L. = +/- 1sigma errors
            [ll, ul] = fcGausLimits( sigma, cl )
            lim = ul*dx
            precision = getErrorPrecision(lim)
            lim = getSignificant(lim, precision)
            lim = '< '+lim+' (' + str(cl) + '% C.L.)'
            s += lim
            
    if sigma < -3:
        print( 'Warning: value highly improbable given uncertainty.' )

    return s


#print printVal(float(sys.argv[1]),float(sys.argv[2]))
