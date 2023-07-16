'''

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Novák
email: peternovaksson@seznam.cz
discord: Goodchilde#1716

'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
#Základní údaje
line = "----------------------------------------"
number_of_texts = len(TEXTS)
users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}


#Přihlášení

name = input("username: ")
password = input("password: ")
print(line)

if name in users.keys():
    if users[name.lower()] == password:
        print(f"Welcom to the app, {name}. ")
        print(f"We have {number_of_texts} to be analyzed. ")
        print(line)
    else:
        print("wrong password, terminating the program..")
        print(line)
        quit()
else:
    print("unregistered user, terminating the program..")
    print(line)
    quit()

#Číslo textu

text_number = input("Enter a number btw. 1 and 3 to select: ")
print(line)
if text_number == "1" or text_number == "2" or text_number == "3":
    text =TEXTS[int(text_number)-1]
else:
    print("Invalid choice, terminating the program..")
    quit()

#Analýza

cleaned_words = list()

for word in text.split():
    cleaned_words.append(word.strip(",.:;"))

tot_words = len(cleaned_words)
title_words= 0
upper_words = 0
lower_words = 0
numeric_words = 0
sum_numeric = 0

for word in cleaned_words:
    if word.istitle():
        title_words += 1
    elif word.isupper():
        upper_words += 1
    elif word.islower():
        lower_words += 1        
    elif word.isdigit:
        sum_numeric += int(word)
        numeric_words += 1

print(f"There are {tot_words} words in the selected text.")
print(f"There are {title_words} titlecase words.")
print(f"There are {upper_words} uppercase words.")
print(f"There are {lower_words} lowercase words.")
print(f"There are {numeric_words} numeric strings.")
print(f"The sum of all the numbers {sum_numeric}.")
print(line)

# spočítám výskyty pro každé slovo
cleaned = []
words = {}

for word in cleaned_words:
    cleaned.append(len(word) * "*")
    
for word in cleaned:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

# získání nejčastějších délek slov
most: list = sorted(
    list(words.values()), reverse=True
)[:13]

# získání slov, která se těchto hodnot týkají
result = list()

for total in words:
    if words[total] in most:
        result.append((words[total], total))

# vypiš výsledky od nejčastější délky slova
print(f"|{'LEN': ^2}|{'OCCURENCES': ^15}|{'NR.': ^2}|")
for index, res in enumerate(sorted(result, reverse=True), 1):
    print(f"|{len(res[1]): ^3}|{res[1]: ^15}|{res[0]: ^2}x|")
