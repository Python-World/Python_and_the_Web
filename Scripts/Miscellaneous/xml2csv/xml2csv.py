from xmltodict import parse as parseXML
from csv import writer as CSVWriter
import json
from sys import argv

xmlPath = ""
csvPath = ""

if len(argv) == 1:
    xmlPath = input("please enter the path to your XML file: ")
    csvPath = input("please enter the path to your CSV file: ")
elif len(argv) == 2:
    xmlPath = argv[1]
    csvPath = input("please enter the path to your CSV file: ")
elif len(argv) >= 3:
    xmlPath = argv[1]
    csvPath = argv[2]

print("started to convert your file...")

xmlFile = open(xmlPath, "r")
data_dict = parseXML(xmlFile.read())
data_root = data_dict[list(data_dict.keys())[0]]
itemsList = list(data_root.values())[0]
print(len(itemsList))
xmlFile.close()

csvFile = open(csvPath, "w")
csvWriter = CSVWriter(csvFile)

count = 0
for item in itemsList:
	item = json.loads(json.dumps(item))
	if count == 0:
		header = item.keys()
		csvWriter.writerow(header)
		count += 1
	csvWriter.writerow(item.values())
csvFile.close()

print(f"done, your file is now on {csvPath}")
