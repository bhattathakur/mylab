given=input("Given value of energy      : ")
expec=input("Expected value of energy   : ")
used=input("Present value of kev/chn    : ")
print("kev/chn multiplier          :",round(float(expec)/float(given),8))
print("kev/chn new  value          :",round(float(expec)/float(given)*float(used),8))
