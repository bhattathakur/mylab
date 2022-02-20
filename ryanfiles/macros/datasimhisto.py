"""
This macro plots the histogram for the data and simulatation to compare them
"""

#import libraries
import matplotlib.pyplot as plt
import numpy as np

#data and simulation files for the same isotopes
total_rows=16384
isotopes=['am241','ba133','co60','cs137','eu152','na22','pb210','ra226']

#load the data files
for iso in isotopes:
    #data_file='/home/thakur/mylab/ryanfiles/datfiles/'+iso+'.dat'
    data_file='/home/thakur/mylab/ryanfiles/simulated_data/'+iso+'sim.dat'
    simulation_file='/home/thakur/mylab/ryanfiles/simulated_datadec23/'+iso+'sim.dat'
    print("data file\t",data_file)
    print("simulation file\t",simulation_file)
    x,y=np.loadtxt(data_file,skiprows=6,unpack=True,max_rows=total_rows) #data
    x1,y1=np.loadtxt(simulation_file,unpack=True)                        #simulation

    print("x\t",x[:5])
    print("y\t",y[:5])
    print("x\t",x[-5:])
    print("y\t",y[-5:])

    fig,axs=plt.subplots(2,1)

    #detector data 
    axs[0].plot(x,y)
    axs[0].set_xlabel('keV/chn')
    axs[0].set_ylabel('counts')
    axs[0].grid(True)
    #axs[0].title.set_text(iso+' Data Spectrum')
    axs[0].title.set_text(iso+' Simulated Spectrum0')

    #simulation data
    axs[1].plot(x1,y1)
    axs[1].set_xlabel('keV/chn')
    axs[1].set_ylabel('counts')
    axs[1].grid(True)
    axs[1].title.set_text(iso+' Simulation Spectrum')

    fig.tight_layout()
    plt.show()
    wait=input("Enter any key to continue...")
