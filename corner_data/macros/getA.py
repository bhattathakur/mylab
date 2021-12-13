#!/usr/bin/python3

import datetime
from math import *

from getdA    import getdA
from printVal import printVal

def getA(id, start, end):
    # id......: ID of calibration source (several formats acceptable).
    # start...: datetime object containting start time of calibration run (UTC).
    # end.....: datetime object containting   end time of calibration run (UTC).
    
    t0    = datetime.datetime(2018, 4, 1,12, 0, 0, 0, datetime.timezone.utc)
    #this time information is based on the source certificates
    # universal time coordinated(UTC)
    print("t0->\t",t0)
    start = (start - t0).total_seconds()
    end   = (end   - t0).total_seconds()
    print("start->\t",start)
    print("end->\t",end)

    dhlp    =  0 # error in year in seconds (+0.25d if halflife expressed in years)
    if   id == 'na22' or id == 'Na-22' or id == 'Na22':
        print("id->\t",id)
        A   = 43.4e3 # in Bq
        print("A->\t",A)
        dA  =  3 # in percent (~95% C.L. or about 2 sigma)
        dA /=  2 # convert to 1 sigma error
        print("dA->\t",dA)
        hl  =    2.6018*365*86400
        dhl =    0.0022*365*86400
        dhlp=          0.25*86400
        print("hl->\t",hl)
        print("dhl->\t",dhl)
        print("dhlp->\t",dhlp)
    elif   id == 'co60' or id == 'Co-60' or id == 'Co60':
        A   = 38.3e3 # in Bq
        dA  =  3 # in percent (~95% C.L. or about 2 sigma)
        dA /=  2 # convert to 1 sigma error
        hl  = 1925.28*86400
        dhl =    0.14*86400
    elif   id == 'ba133' or id == 'Ba-133' or id == 'Ba133':
        A   = 39.3e3 # in Bq
        dA  =  3 # in percent (~95% C.L. or about 2 sigma)
        dA /=  2 # convert to 1 sigma error
        hl  =   10.551*365*86400
        dhl =    0.011*365*86400
        dhlp=          0.25*86400
    elif   id == 'cs137' or id == 'Cs-137' or id == 'Cs137':
        A   = 44.9e3 # in Bq
        dA  =  3 # in percent (~95% C.L. or about 2 sigma)
        dA /=  2 # convert to 1 sigma error
        hl  =   30.08*365*86400
        dhl =    0.09*365*86400
        dhlp=          0.25*86400
    elif   id == 'eu152' or id == 'Eu-152' or id == 'Eu152':
        A   = 36.9e3 # in Bq
        dA  =  3 # in percent (~95% C.L. or about 2 sigma)
        dA /=  2 # convert to 1 sigma error
        hl  =   13.517*365*86400
        dhl =    0.014*365*86400
        dhlp=          0.25*86400
    elif   id == 'pb210' or id == 'Pb-210' or id == 'Pb210':
        A   = 218e3 # in Bq
        dA  =   4 # in percent (~95% C.L. or about 2 sigma)
        dA /=   2 # convert to 1 sigma error
        hl  =   22.20*365*86400
        dhl =    0.22*365*86400
        dhlp=          0.25*86400
    elif   id == 'ra226' or id == 'Ra-226' or id == 'Ra226':
        A   = 29.7e3 # in Bq
        dA  =  3 # in percent (~95% C.L. or about 2 sigma)
        dA /=  2 # convert to 1 sigma error
        hl  = 1600*365*86400
        dhl =    7*365*86400
        dhlp=          0.25*86400
    elif id == 'am241' or id == 'Am-241' or id == 'Am241':
        A   = 38.8e3 # in Bq
        dA  =  3 # in percent (~95% C.L. or about 2 sigma)
        dA /=  2 # convert to 1 sigma error
        hl  =  432.6*365*86400
        dhl =    0.6*365*86400
        dhlp=          0.25*86400

    dA /= 100 # convert to fractional uncertainty

    [ minus, plus ] = getdA(A, A*dA, hl, dhl, dhlp, start, end)
    minus *= -1
    
    # Average activity integrated over the calibration run time.1
    A  *= hl/log(2) * ( exp(-start*log(2)/hl) - exp(-end*log(2)/hl) ) / (end - start)
    print("A->\t",A)
    dA *= A   # convert to absolute   uncertainty
    print("dA->\t",dA)

    
    print( 'Average source activity.......:', A, '+', plus, '/-', minus, 'Bq' )
    print( '                     or.......:', A, '+/-', dA, 'Bq' )
    print( '                     or.......:', printVal(A, dA), 'Bq' )

    return [ A, dA, minus, plus ]
