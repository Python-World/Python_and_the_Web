from json import load
from yaml import dump
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

xmlFile = open(xmlPath, "r")
jsonValue = load(xmlFile)
xmlFile.close()

csvFile = open(csvPath, "w")
dump(jsonValue, csvFile)
csvFile.close()

print(f"done, your file is now on {csvPath}")
