from json import load
from yaml import dump
from sys import argv

jsonPath = ""
yamlPath = ""

# validated the ammout of args passed from the command line, so I could get the path from both files before starting the script

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

# from line 27 to 29
# I opened the json file 
# after that I load the json string into a real python dict
# after that I closed the json file

jsonFile = open(jsonPath, "r")
jsonValue = load(jsonFile)
jsonFile.close()

# from line 36 to 38 
# I opened (and created if not done) the yaml destination file
# after that I dumped the dict into the yamlFile through pyyaml
# after that I closed the csv file

yamlFile = open(yamlPath, "w")
dump(jsonValue, yamlFile)
yamlFile.close()

print(f"done, your file is now on {yamlPath}")
