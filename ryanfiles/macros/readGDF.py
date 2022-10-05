
def readGDF( gdfFile, isotopes ):
    # gdfFile....: gdf file name with relative path
    # isotopes...: list of lists, each containing an isotope name followed by a branching ratio to parent
    # Returns a list of gamma-rays found in gdf file including gamma-ray
    #  0: energy
    #  1: branching ratio
    #  2: branching ratio error
    #  3: fitted rate
    #  4: fitted rate error
    #  5: immediate parent isotope name
    gammas = []
    found  = False
    print(f"Reading the gef file: {gdfFile} to read the data!!!\n")
    file   = open(gdfFile, 'r')

    # First find gammas associated with isotope and peak number (c#)
    for iso in isotopes:
        file.seek(0)
        """
        In Python, seek() function is used to change the position of the File Handler to given specific
        position. File handler is like a cursor, which defines from where the data has to be read or written in the file
        """
        for line in file:
            #print(line)
            data = line.split()
            #print("data:\n",data)

            if     data[0][0:7] == 'actname':
                if data[1]      == iso[0]:
                    norm = int(data[0][7:])
                    print(f"norm: {norm}")
            elif   data[0][0:6] == 'parent' and int(data[0][6:]) == norm:
                parent = float(data[2])
                print(f"parent: {parent}")
                if parent != iso[1]:
                    print( 'GDFit did not use correct chain intensity' )
                    print( 'You must reconcile GDfit...:', parent )
                    print( 'With the above.............:', iso[1] )
            elif   data[0][0] == 'c' and data[0][1].isdigit():
                c = int(       data[0][1:])
                e = float(     data[1])
            elif ( data[0][0:4] == 'norm' ):
                if ( int(float(data[1])+0.9) == norm ):
                    found = True
                    continue
            elif ( data[0][0:6] == 'intens' ):
                br  = float(   data[1])
                ebr = float(   data[2])
                # This correction is done for Eu-152 decays in NuDat2
            elif ( data[0][0:4] == 'time' ):
                lt  = float(   data[1])
                print(f"lt: {lt}")

            if found:
                gammas.append( [e, br, ebr, c] ) # c to find rate below
                found = False

        # Then find background rate for peak # of each gamma.
        for g in gammas:
            c = g[-1]
            file.seek(0)
            for line in file:
                data = line.split()
                if ( data[0][0:6] == 'bgrate' and int(data[0][6:]) == c ):
                    g[-1] =   float(data[1])   # rate
                    g.append( float(data[2]) ) # error
                    g.append( iso[0] )         # lastly, add in the immediate source of gamma-ray
#    print( 'Energy:Intens:IntensE:BGRate:BGRateE')
#    for g in gamma:
#        print( g )

    return [lt, gammas]
