#!/bin/python3

#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

trials=10000                             #total trails
low=-1;high=1;interval=high-low
test=interval*np.random.rand(trials,3)+low #random number between -1 and 1
print(f"test first three rows:\n{test[:3,:]}")

#x,y,z co-ordiante
x=test[:,0]
y=test[:,1]
z=test[:,2]


#radius
r=np.sqrt(x**2+y**2+z**2)
test=np.column_stack((test,r))  #adding radius to the column
print(f"test first three rows with r:\n{test[:3,:]}")


#dataframe from numpy array
df=pd.DataFrame(test,columns=['x','y','z','r'])
print(f"DataFrame head:\n{df.head()}")

#limit the value of x,y,z in the sphere of radius r<0.5 (bead radius)
df_less=df[df.r<0.5]
print(f"DataFrame df_less head:\n{df_less.head()}")

#plotting df_less
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(df_less.x,df_less.y,df_less.z)
plt.show()

#function to get upward distance
def get_upward_distance(x,y,z,dz=0.001,r=0.5):
    '''
    returns the upward distance from a point to the surface of the sphere
    '''
    d=np.sqrt(x**2+y**2+z**2)
    if z==-0.5: return 1.0 #on the lower surface
    z_up=0
    #print(f"before while z_up: {z_up}")
    while(d<r):
        z+=dz
        #print(f"Inside while z: {z}")
        z_up+=dz
        d=np.sqrt(x**2+y**2+z**2)
    #print(f"after while z_up: {z_up}")
    return z_up

#distance travelled column d_bead
df_less['d_bead']=df_less.apply(lambda x:get_upward_distance(x['x'],x['y'],x['z']),axis=1)
print(f"DataFrame df_less head:\n{df_less.head()}")

#thickness of button
button_thickness=3.0 #mm
df_less['d_button']=button_thickness/2.-df_less['d_bead'] #Thickness of button is 3 mm and thickness above 0 is 1.5 mm
print(f"DataFrame df_less head:\n{df_less.head()}")


##Finding the number of events emitted normally upward from the bead
n_up=df_less.shape[0]
print(f"\nn_upward_through_bead:{n_up}\n")


#information to get the probablity of scattering
#Probabality of scatering from the button
button_density=1.18    #g/cm^3 (from simulation data)

#mu data from the nist.gov
button_mu_pb=0.1967    # cm^2/g 47 keV pb-210
button_mu_am=0.1815    #60 keV am-241

#lambda calculation for acrylic button  (C5H802)
#fMaterialsManager->AddMaterial("Acrylic","C5-H8-O2",1.18*g/cm3,"");
#density is from oldmc

button_lambda_pb=1.0*button_mu_pb/button_density #cm
button_lambda_am=1.0*button_mu_am/button_density #cm

#trnasmission factors
transmission_pb=0.964   #47 keV pb-210
transmission_am=0.958   #60 keV am-241


def button_transmission_prob(x,lam):
    return (1-np.exp(-1.0*x/lam))

#number of events
N_emitted_bead=df_less.shape[0]
print(f"N_emitted_bead: {N_emitted_bead}")
N_through_button=N_emitted_bead
print(f"N_though_button: {N_through_button}")


