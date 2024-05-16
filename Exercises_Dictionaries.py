#KW20_Tuple_Dictionaries

#1. Ein Dictionary mit den Vornamen und dem Alter (Ganzzahl) von 5 Personen ist zu erstellen.
#Der Vorname ist der Schlüssel und das Alter der Wert in diesem Dictionary.
#Das Dictionary ist als Ganzes auf der Konsole auszugeben. Anschließend sind in einer Schleife
#nacheinander alle Elemente als Schlüssel-Werte-Paar auszugeben.

name_age_dict = {   "Hans": 26,
                    "Jochen": 30,
                    "Jürgen": 35,
                    "Manuel": 40,
                    "Moritz": 55}

print(name_age_dict)

for name in name_age_dict.items():
    print(name)

#2. Eine Person hatte Geburtstag und das Alter dieser Person soll um 1 erhöht werden. Das
#   Schlüssel-Werte-Paar zu dieser Person soll vor und nach der Änderung ausgegeben werden.

jochen = "Jochen"
print(f"\n('{jochen}', {name_age_dict['Jochen']})\n")
name_age_dict["Jochen"] += 1
print(f"('{jochen}', {name_age_dict['Jochen']})\n")

#3. Alle Namen der Personen sollen ohne Alter auf der Konsole ausgegeben werden.

print(name_age_dict.keys())

#4. Für alle Personen im Dictionary soll auch die Telefonnummer ergänzt werden.
#   Dazu kann ein weiteres Dictionary angelegt werden, in dem die Schlüssel Geburtsjahr und
#   Telefon verwendet werden, z.B. {"Geburtsjahr": 1985, "Telefon": "0151 23456"}. Mit diesen
#   Angaben ist die Altersangabe zu überschreiben. Für die weiteren Personen sind diese
#   Änderungen ebenfalls vorzunehmen. Das Personen-Dictionary ist komplett auszugeben.

print(name_age_dict.values())
i = 0
year_tel_dictlist = [{"Geburtsjahr": 1990, "Telefon":5677},{"Geburtsjahr": 1980, "Telefon":5627},
                {"Geburtsjahr": 1975, "Telefon":5697},{"Geburtsjahr": 1994, "Telefon":5177},
                {"Geburtsjahr": 1999, "Telefon":5377}]

for key in name_age_dict.keys():
    name_age_dict[key] = year_tel_dictlist[i]
    i += 1

print(f"Dictionary :\n{name_age_dict}".replace("{","").replace("}","").replace("'",""))


#5. Eine Person hat 2 Telefonnummern. Es ist eine Liste mit den beiden Telefonnummern zu
#   erstellen und anschließend der bestehende Eintrag Telefon mit der Liste der
#   Telefonnummern zu ersetzen. In einer Schleife sind nacheinander alle Elemente als Schlüssel-
#   Werte-Paar auszugeben.

year_tel_dictlist2 = [1232412,45677]

name_age_dict["Hans"]["Telefon"] = year_tel_dictlist2
    
print(f"Dictionary :\n{name_age_dict}".replace("{","").replace("}","").replace("'","").replace("[","").replace("]",""))