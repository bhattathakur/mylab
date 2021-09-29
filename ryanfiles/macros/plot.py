#!/usr/bin/python3

from array import array
from math  import *
import os
import sys
import ROOT

binWidth = 1 # keV
nchn = 16384

def read( rootFile, gdfFile, datFile  ):
    file = open( gdfFile, 'r' )
    lines = file.readlines()
    keV_chn = float( lines[-8].split()[1] )
    chn_0   = float( lines[-7].split()[1] )
    quad_cal= float( lines[-6].split()[1] )
    cube_cal= float( lines[-5].split()[1] )

    file = rootFile
    c1   = ROOT.TCanvas("c1")
    #print ( 'Processing file.........:', file )
    f = ROOT.TFile.Open( file, 'read' )
    if f.IsZombie():
        print ( file, 'a zombie' )
        return 0
    elif not ROOT.gROOT.FindObject('tT1'):
        print ( file, 'contains no tT1' )
        return 0
    else:
        bins = []
        for bin in range(0,nchn+1):
            e  = chn_0
            e += bin * keV_chn
            e += pow(0.001*bin,2) * quad_cal 
            e += pow(0.001*bin,3) * cube_cal 
            bins.append(e)
        #h1 = ROOT.TH1D("h1", os.getcwd(), nchn, chn_0, chn_0 + nchn*keV_chn)
        h1 = ROOT.TH1D("h1", os.getcwd(), nchn, array('d',bins) )
        h1.SetName("h1")
        t = f.Get('tT1')
        #t.Draw("TrueEnergy*1000>>h1")
        t.Draw("Energy*1000>>h1")
        ngen = t.GetEntries()
        
    file = open( datFile, 'w' )
    for bin in range( 0, h1.GetNbinsX() ):
        file.write( '{:5d} {:20d}\n'.format(bin, int(h1.GetBinContent(bin))) )
    file.close()
    #h1.Scale(864000./ngen);# 10 Bq for 1 dz
    c1.SetLogy()
    c1.Update()
    print ( 'Number generated........:', ngen )
    wait = input('Press any key to continue...')

# main:
print('Input ROOT file name, final (fit result) gdf file name, output dat file name')
read( sys.argv[1], sys.argv[2], sys.argv[3] )

