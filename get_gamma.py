'''
This program displays the gamma radiation from a particular nuclei based on the website
https://www.nndc.bnl.gov/nudat2/

'''
#libraries
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import csv

#url template
url='https://www.nndc.bnl.gov/nudat2/decaysearchdirect.jsp?nuc={}&unc=nds'

#user input for nuclei
nuclei=input("Enter the nuclei:\t")

#request for the url
response=requests.get(url.format(nuclei))            #request for a web page
soup=BeautifulSoup(response.text,'html.parser')         #creating the soup object with given page
table_tag=soup.find('table')
table_rows=table_tag.find_all('tr')
table_rows[1].find("td",class_="su")
desired=table_rows[2]
all_td=desired.find_all('td')
mass_no,atom_no=all_td[0].get_text(separator=" ").split()
symbol=all_td[1].get_text()
print("NUCLEI:\n",mass_no+symbol+atom_no)

#print all information for x-ray and gamma
utags=soup.find_all('u',text='Gamma and X-ray radiation')
x_and_gamma=utags[0].parent.next_sibling.text
#print(x_and_gamma) #x-ray and gamma ray

for utag in utags:
    #print(utag.text,"\n")
    #parent=utag.parent.parent
    #print("parent\t",utag.parent)
    print("next-sibling\n",utag.parent.next_sibling.text)

#save only gamma in the file
temp_file="temp.txt"
final_file="test.txt"
header='Energy  (keV)Intensity  (%)Dose ( MeV/Bq-s )'

with open(temp_file,'w') as f:
    f.write(x_and_gamma)

rev_str=""
print("open in the reversed order and save the desired one:\n")
with open(final_file,'w') as f:
    for line in reversed(list(open(temp_file))):
        if line[0]=='X':break
        #print(line.rstrip())
        rev_str=line+rev_str
    f.write(header+"\n")
    f.write(rev_str)
# with open(final_file,'w') as f:
#     f.write()
#     for s in rev_str:
#         f.write(s)
# #with open(final_file) as f:
#     f.write(rev_str)
print("GAMMA LIST")
print(100*'-')
print(rev_str)

#display the gammas as the dataframe
df=pd.read_csv("test.txt",delimiter="\t")
print("data-frame\n",df)
