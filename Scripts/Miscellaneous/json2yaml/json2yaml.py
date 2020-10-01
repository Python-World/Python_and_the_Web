from json import load
from yaml import dump
from sys import argv

jsonPath = ""
yamlPath = ""

if len(argv) ==1:
	jsonPath = input("please enter the path to your JSON file: ")
	yamlPath = input("please enter the path to your YAML file: ")
elif len(argv) == 2:
    jsonPath = argv[1]
    yamlPath = input("please enter the path to your YAML file: ")
elif len(argv) >= 3:
	jsonPath = argv[1]
	yamlPath = argv[2]

print("started to convert your file...")

jsonFile = open(jsonPath, "r")
jsonValue = load(jsonFile)
jsonFile.close()

yamlFile = open(yamlPath, "w")
dump(jsonValue, yamlFile)
yamlFile.close()

print(f"done, your file is now on {yamlPath}")
