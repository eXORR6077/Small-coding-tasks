#Aufgabe 1

#Namen und Geschlecht + Uhrzeit

morgen = "Guten Morgen"
mittag = "Guten Tag"
abend = "Guten Abend"
name_input = input("Bitte gib deinen Namen ein: ")
time_input = int(input("Wie spät ist es? Bitte nur die Stunde angeben: "))
gender_input = input("Bitte gib dein Geschlecht wie in den Klammern an \n(<Mann> , <Frau>, <Divers>): ")

if time_input <= 9:
        time = morgen
elif time_input <= 17:
        time = mittag
elif time_input <=24:
        time = abend
else:
    time_input = input("Bitte nur volle Stunden!")

match gender_input:
    case "Mann":
        gruß = "Herr"
    case "Frau":
        gruß = "Frau"
    case "Divers":
        gruß = "Herr/Frau"
    case _:
        gender_input = input("Bitte gib dein Geschlecht wie in den Klammern an \n(<Mann> , <Frau>, <divers>): ")
        
print(f"{time}, {gruß} {name_input}!")





