#!/usr/bin/python3

import math
import sys

from getRatioError import getRatioError
from printVal      import printVal

parent = sys.argv[1]

print("data "+parent+" ...")
# Read all entries from data.dat,
# then remove earlier superseeded entries.
data = []
file = open('data.dat', 'r')
for line in file:
    words = line.split()
    if words[0] != parent:
        continue
    data.append([
        [ words[0],         # 0: parent
          words[1] ],       # 0: isotope
        float(words[ 2]),   # 1: energy
        float(words[ 6]),   # 2: source activity (decayed)
        float(words[ 7]),   # 3: uncertainty in source activity
        float(words[ 8]),   # 4: total activity error (minus)
        float(words[ 9]),   # 5: total activity error (plus)
        float(words[10]),   # 6: branching ratio
        float(words[11]),   # 7: error
        float(words[12]),   # 8: rate
        float(words[13]) ]) # 9: error
for entry in reversed(range(len(data))):
    for e in range(entry):
        # If this entry's isotope and energy match a later one, then remove it.
        if data[e][0] == data[entry][0] and data[e][1] == data[entry][1]:
            data.remove(data[e])
            break


        
# Read all entries from sim.dat,
# then remove earlier superseeded entries.
simu = []
print("simulation "+parent+" ...")
file = open('sim.dat', 'r')
for line in file:
    words = line.split()
    if words[0] != parent:
        continue
    simu.append([
        [ words[0],         # 0: isotope
          words[1] ],       # 0: isotope
        float(words[ 2]),   # 1: energy
        int(  words[ 6]),   # 2: number generated
        float(words[ 7]),   # 3: livetime assumed by GDFit
        float(words[ 8]),   # 4: branching ratio
        float(words[ 9]),   # 5: error
        float(words[10]),   # 6: rate
        float(words[11]) ]) # 7: error
for entry in reversed(range(len(simu))):
    for e in range(entry):
        # If this entry's isotope and energy match a later one, then remove it.
        if simu[e][0] == simu[entry][0] and simu[e][1] == simu[entry][1]:
            simu.remove(simu[e])
            break

        

# Confirm each gamma-ray appears in both the data and simulation analysis.
for s in range(len(simu)):
    found = False
    for d in range(len(data)):
        if data[d][0] == simu[s][0] and data[d][1] == simu[s][1]:
            found = True
            break
    if not found:
        simu.remove(simu[s])
        print( 'Warning: '+simu[s][0][1],simu[s][1],'keV gamma-ray not found in data.')

for d in range(len(data)):
    found = False
    for s in range(len(simu)):
        if data[d][0] == simu[s][0] and data[d][1] == simu[s][1]:
            found = True
            data[d].append(simu[s])
            if (simu[s][4] != data[d][6] and simu[s][5] != data[d][7]):
                print('Warning: '+simu[s][0][1],simu[s][1],'keV gamma-ray branching ratio/error differs.')
            break
    if not found:
        data.remove(data[d])
        print( 'Error: '+data[d][0][1],data[d][1],'keV gamma-ray not found in simulation.')
        exit(-1)

print('opening correction.dat...')
file = open('correction.dat','a')
for d in data:
    # Get the error on the ratio by simulation.
    A        = d[2]
    dA       = d[3]
    lo       = d[4]
    hi       = d[5]
    br       = d[6]
    ebr      = d[7]
    r        = d[8]
    er       = d[9]
    N        = d[-1][2]
    livetime = d[-1][3]
    s        = d[-1][6]
    es       = d[-1][7]
    num      = N/livetime*r
    enum     = N/livetime*er
    denom    = A*s
    # Branching ratio cancels in the data/simulation ratio.
    # But the simulation uses some branching ratio so add it to the
    # simulation 'rate' (in the denominator).
    edenom   = ebr*ebr/(br*br) + es*es/(s*s) # temporary value
    A2       = A*A
    [ minus1, plus1 ] = getRatioError( num, enum, enum,
                                       denom,
                                       denom*math.sqrt( lo*lo/A2 + edenom ),
                                       denom*math.sqrt( hi*hi/A2 + edenom ) )
    [ minus2, plus2 ] = getRatioError( num, enum, enum,
                                       denom,
                                       denom*math.sqrt(            edenom ),
                                       denom*math.sqrt(            edenom ) )
    c = num/denom
    print( 'Efficiency correction.:', c,
           '+',  plus1 - c,
           '/-', c - minus1 )
    print( '                   or.:', printVal( c, (plus1-minus1)/2 ) )

    file.write( '{:6s} {:6s} {:.4f} {:e} {:e} {:e} {:e} {:e} {:e} {:e}\n'.format(d[0][0], d[0][1], d[1], c, c-minus1, plus1-c, c-minus2, plus2-c, lo/A, hi/A) )
file.close()
