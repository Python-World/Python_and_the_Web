
"""
Created on Thu Aug 20 20:27:24 2020

@author: Incognito
"""

import requests
import os
def download(fileName):
    f = open(fileName,'wb')
    f.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'Incognito'}).content)
    f.close()
    
n=int(input("Enter no. of images to download: "))
print("1.Specify path to a directory to store the images")
print("2.Create a directory to store the images")
ch=int(input("Enter option:"))
if(ch==1):
    dir=input("Enter path to directory: ")
    for i in range(n):
        download('person'+str(i+1)+'.jpg')
else:
    parent=input("Enter parent directory: ")
    new=input("Enter directory name to be created: ")
    dir=os.path.join(parent, new)
    os.mkdir(dir)
    print("Directory '% s' created" % new)
    print(dir)
    for i in range(n):
        download(dir+"/"+'person'+str(i+1)+'.jpg')
