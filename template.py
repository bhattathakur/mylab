#This program prints the template for the gdf file
num="0."+12*"0"+"E+00"
file_name="template.gdf"

#print("num\n",num)

#open the file
f=open(file_name,'w')

lim=40
for i in range(lim):
    if i==0:
     print("ero"+"\t\t"+num+"\t"+num)
     f.write("ero"+"\t\t"+num+"\t"+num+"\n")
    print("ero"+str(i+1)+"\t\t"+num+"\t"+num)
    f.write("ero"+str(i+1)+"\t\t"+num+"\t"+num+"\n")

for i in range(lim):
    print("actname"+str(i+1)+"\t"+"activ"+str(i+1)+"\t\t\t"+"0")
    f.write("actname"+str(i+1)+"\t"+"activ"+str(i+1)+"\t\t\t"+"0"+"\n")
for i in range(lim):
    print("parent"+str(i+1)+"\t\t"+"0"+"\t"+"0")
    f.write("parent"+str(i+1)+"\t\t"+"0"+"\t"+"0"+"\n")

for i in range(lim):
    print("activ"+str(i+1)+"\t\t"+4*(num+" "))
    f.write("activ"+str(i+1)+"\t\t"+4*(num+" ")+"\n")

for i in range(lim):
    print("bgrate"+str(i+1)+"\t\t"+4*(num+" "))
    f.write("bgrate"+str(i+1)+"\t\t"+4*(num+" ")+"\n")

for i in range(lim):
    print("const:"+str(i+1)+"\t\t"+4*(num+" "))
    print("lin:"+str(i+1)+"\t\t"+4*(num+" "))
    print("x^2:"+str(i+1)+"\t\t"+4*(num+" "))
    f.write("const:"+str(i+1)+"\t\t"+4*(num+" ")+"\n")
    f.write("lin:"+str(i+1)+"\t\t"+4*(num+" ")+"\n")
    f.write("x^2:"+str(i+1)+"\t\t"+4*(num+" ")+"\n")

for i in range(lim):
    print("c"+str(i+1)+"\t\t"+4*(num+" "))
    print("sigma"+str(i+1)+"\t\t"+4*(num+" "))
    print("norm"+str(i+1)+"\t\t"+4*(num+" "))
    print("branch"+str(i+1)+"\t\t"+4*(num+" "))
    f.write("c"+str(i+1)+"\t\t"+4*(num+" ")+"\n")
    f.write("sigma"+str(i+1)+"\t\t"+4*(num+" ")+"\n")
    f.write("norm"+str(i+1)+"\t\t"+4*(num+" ")+"\n")
    f.write("branch"+str(i+1)+"\t\t"+4*(num+" ")+"\n")

name_list=["kev/chn","chn_0","sigfact","sigofst","time","stats"]

for i in name_list:
    if i=="stats":
        print(i+"\t\t"+3*(num+" "))
        f.write(i+"\t\t"+3*(num+" ")+"\n")
    else:
        print(i+"\t\t"+4*(num+" "))
        f.write(i+"\t\t"+4*(num+" ")+"\n")
#close the file
f.close()
