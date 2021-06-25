#read the values related to given isotope
#file_name=input("background file: ")
file_name="ra226"
file_name=file_name+".gdf"
print("file-name\t:",file_name)
num=input("activity#: ")
print("file_name\t",file_name,"\n")
desired_terms=['eroi','actname','parent','activ','bgrate','c','norm','sigma','norm','branch','cnst:','lin:','x^2:','const:','kev/chn','chn_0','quad_cal','cube_cal','sigrootE','sigofst','time','stats']
#peak_parameters=['c','sigma','activ','branch']
#poly_back_parameters=['cnst:','lin:','x^2:']
#activity_parameter=['activ']
#print("desired_terms\t",desired_terms)
desired_terms=[i+num for i in desired_terms[:-8]]+[i for i in desired_terms[-8:]]
#print("modified desired terms\n",desired_terms)
#peak_parameters=[i+num for i in peak_parameters]
#poly_back_parameters=[i+num for i in poly_back_parameters]
#peak_param=[]
#poly_back=[]
#print("desired_terms\t",desired_terms)
#print(50*"==")
important_lines=[]
with open(file_name) as f:
    for line in f:
        first_word=line.split(" ",1)[0]
        if first_word in desired_terms:
            #print(line.strip())
            #save important lines
            important_lines.append(line.strip())
        
        #print("first word\t",first_word)
        #counter=0
        #print("Peak Parameters\n")
        #if first_word in peak_parameters:
        #    #print(line)
        #    peak_param.append(line)
        #    #counter=counter+1
        #if first_word in poly_back_parameters:
        #    poly_back.append(line)
        #    #print(line)

#print(50*"==")
#print("Peak Parameters\n")
#for i in peak_param:
#    print(i.strip())
#print("Polygonal Background Parameters\n")
#for i in poly_back:
#    print(i.strip())
#print(50*"==")
print("important_lines\n")
for c,i in enumerate(important_lines):
    print(str(c)+": ",i)

#print(50*"--")
print("FIT PARAMETERS\n")
def print_parameters(title,lis):
    print(90*'-')
    print(title)
    for i in lis:
        print(important_lines[i].strip())
    
#important parameters
act=[1]
parent=[2]
bgrate=[4]
peakparam=[8,9,10,11] #cj,sigmaj,activj,branchj
polyparam=[5,6,7] #cnst:k,lin:k,x^2:k
globalparam=[12,13,14,15,16,17,18,19]#kev/chn,eoffset,quadcal,sigfact,sigoffset,timepar
roi=[0] #ROI

#test fuction
print_parameters("ROI",roi)
print_parameters("Activity Name:",act)
print_parameters("Parent Name:",parent)
print_parameters("Peak Parameters: ",peakparam)
print_parameters("Poly Parameters: ",polyparam)
print_parameters("Global Parameters: ",globalparam)
