#!/usr/bin/env python3
import re

print("Enter the name of the input file: ")
file=str(input())

try:
    f = open(file,"r")
except FileNotFoundError:
    print("File does not exists")

email={}

for i in f:
    em = re.findall('\S+@\S+\.\S+',i)
    for j in em:
        email[j]=email.get(j,0)+1
        print(j)

f.close()
