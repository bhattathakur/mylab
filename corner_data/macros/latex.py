from string import Template
sim=[
'am241_sim.pdf',
'ba133_sim.pdf',
'co60_sim.pdf' ,
'cs137_sim.pdf',
'eu152_sim.pdf',
'na22_sim.pdf' ,
'pb210_sim.pdf',
'ra226_sim.pdf'
]

data=[
'dataam241.pdf',
'databa133.pdf',
'dataco60.pdf' ,
'datacs137.pdf',
'dataeu152.pdf',
'datana22.pdf' ,
'datapb210.pdf',
'datara226.pdf'
]
temp=Template("""
    \\begin{figure}[htb!])
    \\begin{subfigure}[b]{0.5\\textwidth}
    \\includegraphics[width=\\linewidth]{dataeff/$dat}
    \\end{subfigure}
    \\begin{subfigure}[b]{0.5\\textwidth}
    \\includegraphics[width=\\linewidth]{simeff/$si}
    \\end{subfigure}
    \\caption{$na}
    \\end{figure}
    """)

for i in range(len(data)):
    s=sim[i]
    idx=s.find('_')
    s=s[:idx]
    print('%'+s)
    print(temp.substitute({'dat':data[i],'si':sim[i],'na':s}))
#print(temp.substitute({'what':'test','yes':'no'}))

#print(temp.format("hello"))
#print(temp)
#print(temp.format("test"))
#for i in range(8):
#    s="""
#    \\begin{figure}[htb!])
#    \\begin{subfigure}[b]{0.5\\textwidth}
#    \\includegraphics[width=\\linewidth]{dataeff/{}}"""
#    #\\end{subfigure}
#    #\\begin{subfigure}[b]{0.5\\textwidth}
#    #\\includegraphics[width=\\linewidth]{simeff/{}}
#    #\\end{subfigure}
#    #\\caption{na22}
#    #\\end{figure}
#    #"""
#    print(s.format("hello"))
#
