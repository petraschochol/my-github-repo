text1 = ['''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''']

text2 = ['''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''']

text3 = ['''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

text = (text1, text2, text3)
clanek = []

odd = 80*"="
print(odd)
# Definice uživatelů
data = {
        'uzivatel1': 'heslo',
        'bob': '123',
        'ann': 'pass123',
        'mike': 'password123',
        'liz': 'pass123'
        }

# Zeptej se na uzivatelske jmeno a heslo
jmeno = input("Enter your name : ")
heslo = input("Enter your password : ")

print(odd)
# Ověření uživatele
if data.get(jmeno) == heslo:
    print(f"Hello {jmeno} ! Your username and password is Ok. You can continue analyzing...")
    index = int(input("Enter a number btw 1 and 3 to select : "))
    if index == 1:
        print("Ok. Text 1 has been selected !")
    elif index == 2:
        print("Ok. Text 2 has been selected !")
    elif index == 3:
        print("Ok. Text 3 has been selected !")
    else:
        print("The text that was selected is not in database ! Program will be ended !")
        quit()
else:
    print("Your username or password is bad! The program will end immediately!")
    quit()

# Uprava textu
text = str(text[(index - 1)])
clanek = text.replace('\\n', ' ').replace(',', ' ').replace('.', ' ').strip('."\'][').split(" ")

# Pocitadla
count = 0
pocet_t = 0
pocet_u = 0
pocet_l = 0
soucet = 0
cislo = ""
cisla = []
cetnost = dict()

# Prochazeni a indexovani slov v textu
for i, slovo in enumerate(clanek, 1):
    if len(slovo) == 0:
        count += 1
        continue

    else:
        # Cetnost vyskytu v textu
        if len(slovo) in cetnost:
            cetnost[(len(slovo))] += 1
        else:
            cetnost.setdefault(len(slovo))
            cetnost[(len(slovo))] = 1

        for char in slovo:
            if char.isdigit():
                cislo = cislo + char
            else:
                if cislo == "":
                    continue
                else:
                    cisla.append(cislo)
                    cislo = ""

        if slovo.istitle():
            pocet_t += 1

        elif slovo.isupper():
            pocet_u += 1

        elif slovo.islower():
            pocet_l += 1

# Soucet cisel z textu
for num, c in enumerate(cisla, 1):
    soucet += int(c)

# Tisk vysledku
print(odd)
print(f"There are {i-count} words in the selected text.")
print(f"There are {pocet_t} titlecase words.")
print(f"There are {pocet_u} all uppercase chars.")
print(f"There are {pocet_l} all lowercase chars.")
print(f"There are {num} numeric strings.")
print(f"The sum of all the numbers {soucet}.")

# Sloupcovy graf
print(odd)
print(f"    LEN |     OCCURENCES     |  NR.  ")
print(odd)

for i in range(1, 21):
    if i in cetnost.keys():
        mezera = 20-(int(cetnost[i]))
        print(f"  {i:>5} |{cetnost[i]*'*'}{mezera*' '}|  {cetnost[i]   }")
    else:
        continue
