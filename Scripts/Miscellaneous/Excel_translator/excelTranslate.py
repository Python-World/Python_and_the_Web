import googletrans
from googletrans import Translator
import pandas as pd
# print(googletrans.LANGUAGES)
langs = googletrans.LANGUAGES
reverseCode = {}
for key, value in langs.items():
    reverseCode[value] = key


done = False
while not done:
    fname = input('Please enter the name of your file(with extension): ')
    try:
        data = pd.read_excel(fname)
        done = True
    except FileNotFoundError:
        print("This file doesn't exist. Please check name again.")
    #except Exception:
    #    print("Some error occured...")
        
        
done = False
while not done:
    fromLang = input("Which is the original language? ")
    try:
        fromLang = reverseCode[fromLang]
        done  = True
    except KeyError:
        print("This language is not supported.")
        print()
        print("Supported Languages: ", reverseCode.keys())
    #except Exception:
    #    print("Some error occured.")
        
        
done = False
while not done:
    toLang = input("Which language to translate in? ")
    try:
        toLang = reverseCode[toLang]
        done  = True
    except KeyError:
        print("This language is not supported.")
        print()
        print("Supported Languages: ", reverseCode.keys())
    #except Exception:
    #    print("Some error occured.")
    

coltochange = []

while True:
    col = input("Choose column name you want to change(choose only one column at a time)(e to end): ")
    if col in ['e', 'E']:
        print('\n\n') 
        break
    if col in data.columns:
        coltochange.append(col)
    else:
        print("This column doesn't exist. Please recheck the name...")

# pr = input("Do you want to print pronounciations in terminal of converted text to check? (y/n)")


translator = Translator()

for index in data.index:
    try:
        for col in coltochange:
            lineres = translator.translate(data[col][index], src=fromLang, des=toLang)
            data[col][index] = lineres.text
            # if pr == 'y': print(lineres.pronunciation)
        
    except Exception as e:
        print("Error occured")
        print(e)
        break
    
writer = pd.ExcelWriter('result.xlsx',  engine ='xlsxwriter') # pylint: disable=abstract-class-instantiated
data.to_excel(writer, sheet_name ='Sheet1') 
writer.save() 
