#import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

inputfile="en_eff_error.csv"
header=["energy","efficiency","error"]
df=pd.read_csv(inputfile,names=header)
print(df)

#plt.plot(df.energy,df.efficiency,'go')
fig,ax=plt.subplots(figsize=(10,8))
ax.errorbar(df.energy,df.efficiency,yerr=df.error,fmt='.',ecolor='r')
ax.set_xlabel("Energy (keV)");ax.set_ylabel("Efficiency (%)")
# zip joins x and y coordinates in pairs
#xs=df.energy;ys=df.efficiency
#for x,y in zip(xs,ys):
#    label = "{:.2f}".format(x)
#    plt.annotate(label, # this is the text
#                 (x,y), # these are the coordinates to position the label
#                 textcoords="offset points", # how to position the text
#                 xytext=(0,-20), # distance from text to points (x,y)
#                 ha='center') # horizontal alignment can be left, right or center
xtickval=list(df.energy)
print("xtickval\t",xtickval)
#locs,labels=plt.xticks() #current tick location and labels
locs=list(ax.get_xticks())
print("locs\n",locs)
#labs=ax.get_xlabel()
newlocs=locs+xtickval
newlabels=[str(x) for x in newlocs]
#print("new location\t",newlocs)
print("new label\n",newlabels)
#print("new labels\t",newlabels)
#
#plt.xticks(list(plt.xticks()[0])+xtickval)
#xtickname=[str(x) for x in xtickval]
#print("xtick-values",xtickval)
#print("xtick-names",xtickname)
#plt.xticks(xtickval,xtickname,rotation='vertical')
#locs,labels=xticks()
#locs=ax.get_xticks()
ax.set_xticks(ticks=newlocs)
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
#ax.set_xticklabels(newlabels,rotation=45)
#plt.rcParams["figure.figsize"]=(10,16)
plt.title("Ra-226 at door")
plt.savefig('ra226effvsenergy.pdf')
plt.show()



