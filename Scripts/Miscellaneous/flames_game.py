# input two names
name1 = input('Enter first name: ')
name2 = input('Enter second name: ')

# convert to uppercase
name1List = list(name1.upper())
name2List = list(name2.upper())

flames = list('FLAMES')
result = ['Friends', 'Lovers', 'Acquaintance', 'Marriage', 'Enemy', 'Siblings']

for letter in name1List:
    if letter in name2List:
        # check for common letters
        print('Checking', letter, '...')
        print('Letter ', letter, ' found')

        # find & replace the letter to show it has been striked out
        index1 = name1List.index(letter)
        name1List[index1] = '_'
        index2 = name2List.index(letter)
        name2List[index2] = '_'
        print('Replaced ', letter)

names = name1List + name2List