input_file="am241.dat"

f=open(input_file,'r')
lines=f.readlines()
f.close()

print("readlines result:\n",lines[2])

print("split the lines result:\n",lines[2].split())
