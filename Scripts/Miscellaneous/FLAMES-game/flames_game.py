# input two names
name1 = input('Enter first name: ')
name2 = input('Enter second name: ')

# convert to uppercase
name1List = list(name1.upper())
name2List = list(name2.upper())

flames = 'FLAMES'
flamesList = list('FLAMES')
f = 'FLAMES'
fList = list('FLAMES')
resultList = ['Friends', 'Lovers', 'Acquaintance', 'Marriage', 'Enemy', 'Siblings']

for letter in name1List:
    if letter in name2List:
        # check for common letters
        print('Checking ', letter, '...')
        print('Letter ', letter, ' found')

        # find & replace the letter to show it has been striked out
        index1 = name1List.index(letter)
        name1List[index1] = '_'
        index2 = name2List.index(letter)
        name2List[index2] = '_'
        print('Replaced ', letter)

print(name1List)
print(name2List)

names = name1List + name2List
count = 0

for letter in names:
    # count all characters other than replaced/spaces
    if(letter != '_' and letter != ' '):
        count+=1

print(count)

index = 0

while len(flames) > 1:
    for i in range(count):
        index += 1
        if index > len(flames):
            # if index crosses length of 'flame' then reset it to 1
            index = 1

    flames.remove(flames[index-1])
    index -= 1

print('Your result is: ', flames)