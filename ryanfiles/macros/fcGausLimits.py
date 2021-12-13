#!/usr/bin/python

def fcGausLimits(sigma, cl=90):
    cl68 = [ ]
    cl90 = [ ]
    cl95 = [ ]
    cl99 = [ ]

    with open( 'fcGausLimits.dat' ) as f:
        for line in f:
            input = line.split()
            if len(input) == 10:
                cl68.append( [ float(input[1]), [ float(input[2]), float(input[3]) ] ] )
                cl90.append( [ float(input[1]), [ float(input[4]), float(input[5]) ] ] )
                cl95.append( [ float(input[1]), [ float(input[6]), float(input[7]) ] ] )
                cl99.append( [ float(input[1]), [ float(input[8]), float(input[9]) ] ] )
                cl68.append( [ float(input[0]) ] )
                cl90.append( [ float(input[0]) ] )
                cl95.append( [ float(input[0]) ] )
                cl99.append( [ float(input[0]) ] )
            else:
                cl68[-1] = [ cl68[-1][0], [ float(input[0]), float(input[1]) ] ]
                cl90[-1] = [ cl68[-1][0], [ float(input[2]), float(input[3]) ] ]
                cl95[-1] = [ cl68[-1][0], [ float(input[4]), float(input[5]) ] ]
                cl99[-1] = [ cl68[-1][0], [ float(input[6]), float(input[7]) ] ]
    f.closed

    cl68.sort()
    cl90.sort()
    cl95.sort()
    cl99.sort()

    if cl == 68:
        cl = cl68
    if cl == 90:
        cl = cl90
    if cl == 95:
        cl = cl95
    if cl == 99:
        cl = cl99
    slast = cl[0]
    for s in cl[1:]:
        if sigma <= s[0]:
            m  =  s[1][0] - slast[1][0]
            ds =     s[0] - slast[0]
            m /= ds
            b  = s[1][0] - m*s[0]
            ll = m*sigma + b
            m  = s[1][1] - slast[1][1]
            m /=    s[0] - slast[0]
            b  = s[1][1] - m*s[0]
            ul = m*sigma + b
            break
        slast = s

    return [ll, ul]

