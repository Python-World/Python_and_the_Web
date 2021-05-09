import sys
import time

print("-------F.L.A.M.E.S.-------")

# display output format
print("\nOutput format:")
print(" ['F']: 'Friends', ['L']: 'Love', ['A']: 'Acquaintance', ")
print(" ['M']: 'Marriage', ['E']: 'Enemies', ['S']: 'Siblings', ")

# input two names
name1 = input("\nEnter first name: ")
name2 = input("Enter second name: ")

# convert to uppercase
name1List = list(name1.upper())
name2List = list(name2.upper())

# convert 'FLAMES' into a list
flames = list("FLAMES")

for letter in name1List:
    if letter in name2List:
        # check for common letters
        print("\nChecking " + letter + "...")
        print("Letter " + letter + " found")

        # find & replace the letter to show it has been striked out
        index1 = name1List.index(letter)
        name1List[index1] = "_"
        index2 = name2List.index(letter)
        name2List[index2] = "_"
        print("Replaced " + letter)

print(name1List)
print(name2List)

names = name1List + name2List
count = 0

for letter in names:
    # count all characters other than replaced/spaces
    if letter not in ("_", " "):
        count += 1

index = 0

while len(flames) > 1:
    for i in range(count):
        index += 1
        if index > len(flames):
            # if index crosses length of 'flame' then reset it to 1
            index = 1

    flames.remove(flames[index - 1])
    index -= 1

print("\nYour result is: ", flames)

# wait before exiting
time.sleep(5)
print("Exiting!")
time.sleep(2)
sys.exit()
