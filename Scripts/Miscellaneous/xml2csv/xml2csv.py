from csv import writer as CSVWriter
from json import dumps, loads
from sys import argv

from xmltodict import parse as parseXML


# validated the ammout of args passed from the command line, so I could get the path from both files before starting the script
def getInputAndOutputFiles():
    if len(argv) == 1:
        xmlPath = input("please enter the path to your JSON file: ")
        csvPath = input("please enter the path to your YAML file: ")
    elif len(argv) == 2:
        xmlPath = argv[1]
        csvPath = input("please enter the path to your YAML file: ")
    elif len(argv) >= 3:
        xmlPath = argv[1]
        csvPath = argv[2]
    return xmlPath, csvPath


xmlPath, csvPath = getInputAndOutputFiles()

print("started to convert your file...")


# from line 31 to 35
# I read the file from the xmlPath variable, and got the dictory from parseXML
# After that I got the first key from the dict (asumming the user passed a single xml liked the test.xml file)
# After that I got the list of nodes inside the "root"
# And finally I close the file
def getChildNodesFromRoot():
    with open(xmlPath, "r") as xmlFile:
        data_dict = parseXML(xmlFile.read())
        data_root = data_dict[list(data_dict.keys())[0]]
        itemsList = list(data_root.values())[0]
        return itemsList


itemsList = getChildNodesFromRoot()
# Declared a csvWrite (object to write rows on a csv file)
csvFile = open(csvPath, "w")
csvWriter = CSVWriter(csvFile)


# from line 49 to 57
# I iterated over all the items on the child of the file root
# After that i made the variable item into a real dict so I could use
# .keys and .values, the keys for the header row
# and the values for all other rows on our csv'

count = 0
for item in itemsList:
    item = loads(dumps(item))
    if count == 0:
        header = item.keys()
        csvWriter.writerow(header)
        count += 1
    csvWriter.writerow(item.values())
csvFile.close()

print(f"done, your file is now on {csvPath}")
