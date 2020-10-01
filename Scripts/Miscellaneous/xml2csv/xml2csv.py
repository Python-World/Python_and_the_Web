from xmltodict import parse as parseXML
from csv import writer as CSVWriter
import json
from sys import argv

xmlPath = ""
csvPath = ""

if len(argv) ==1:
	xmlPath = input("please enter the path to your XML file: ")
	csvPath = input("please enter the path to your CSV file: ")
elif len(argv) == 2:
    xmlPath = argv[1]
    csvPath = input("please enter the path to your CSV file: ")
elif len(argv) >= 3:
	xmlPath = argv[1]
	csvPath = argv[2]

print("started to convert your file...")

xmlFile = open(xmlPath,"r")
data_dict = parseXML(xmlFile.read())
xmlFile.close()

csvFile = open(csvPath, "w")
csvWriter = CSVWriter(csvFile)

count = 0
for emp in data_dict: 
    if count == 0: 
        # Writing headers of CSV file 
        header = emp.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(emp.values()) 
csvFile.close()

print(f"done, your file is now on {csvPath}")
