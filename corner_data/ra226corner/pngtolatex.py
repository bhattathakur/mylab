#macro to include bulk of .png files in the latex figureo
unit=\
"""
\\begin{figure}
\\incluegraphics[width=0.5\\linewidth]{0}
\\caption{1}
\\label{2}
\\end{figure}
"""
#print(type(unit))
#print(unit)
#
#print(unit.format("2","3","4"))

#function to create the multiple plots in latex file
def showpngs(filename,caption,label):
    print("\\begin{figure}")
    print("\incluegraphics[width=0.5\linewidth]{"+filename+"}")
    print("\caption{"+caption+"}")
    print("\label{"+label+"}")
    print("\end{figure}")

#root of the png file
ro="ra226.ChnROI"
imgdir="ra226roi/"
#print("working with the function")
for i in range(1,48):
    print("% working for the plot no "+str(i)+"\n")
    root=ro+str(i)
    root1=imgdir+ro+str(i)+".png"
    showpngs(root1,root,root)
    print("\n")

