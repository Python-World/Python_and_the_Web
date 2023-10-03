from json import load
from sys import argv

from yaml import dump


# validated the ammout of args passed from the command line,
# so I could get the path from both files before starting the script
def getInputAndOutputFiles():
    if len(argv) == 1:
        jsonPath = input("please enter the path to your JSON file: ")
        yamlPath = input("please enter the path to your YAML file: ")
    elif len(argv) == 2:
        jsonPath = argv[1]
        yamlPath = input("please enter the path to your YAML file: ")
    elif len(argv) >= 3:
        jsonPath = argv[1]
        yamlPath = argv[2]
    return (jsonPath, yamlPath)


print("started to convert your file...")
jsonPath, yamlPath = getInputAndOutputFiles()


# from line 24 to 26
# I opened the json file
# after that I load the json string into a real python dict
def getJSONValueFromFile(jsonPath):
    with open(jsonPath, "r") as jsonFile:
        return load(jsonFile)


# I opened (and created if not done) the yaml destination file
# after that I dumped the dict into the yamlFile through pyyaml
# after that I closed the csv file
if __name__ == "__main__":
    jsonValue = getJSONValueFromFile(jsonPath)
    yamlFile = open(yamlPath, "w")
    dump(jsonValue, yamlFile)
    yamlFile.close()
    print(f"done, your file is now on {yamlPath}")
