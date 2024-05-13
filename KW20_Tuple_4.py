#KW20_Tupel_4

#4. Lösung überarbeiten
#   Folgende Aufgabe wurde bereits gelöst:
#   Für eine Nachricht soll von einem Programm automatisch die Anrede formuliert werden. Von
#   der Konsole sind Eingaben für Name, Geschlecht und die Uhrzeit als Stundenangabe
#   einzulesen  Die Anrede soll je nach Tageszeit mit „Guten Morgen“ (0–9 Uhr), „Guten Tag“
#   (10–17), „Guten Abend (18–0 Uhr) beginnen und anschließend mit „Herr xxx“ bzw. „Frau xxx“
#   fortgesetzt werden. Für xxx soll der entsprechende Name eingesetzt werden
#   Das Programm ist so anzupassen, dass die Überprüfung auf gültige Eingaben (wie z.B.: m, w,
#   d, M, Mann, f, Frau, …) mit Hilfe eines Tupels der zugelassen Werte durchgeführt wird.
#   Ebenfalls sollen die Begrüßungsformeln (Guten Morgen, Guten Tag und Guten Abend) in
#   einem Tupel definiert werden und die Anrede mit entsprechenden Zugriffen daraus
#   zugesetzt werden.

def inputs():
    in_name = input("Bitte gib deinen Nachnamen ein:\n")
    in_gender = input("Bitte gib dein Geschlecht ein:\n").lower()
    in_time = int(input("Wie spät ist es?\n(Bitte volle Stunde(0-23)):\n"))
    return in_gender, in_name, in_time

#Tuples
t_gender = ("m","male","männlich","mann","w","female","f","weiblich","frau","d","divers")
t_time = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)
t_greetings = ("Moin", "Tach", "Nabend")
t_Anrede = ("Herr", "Frau")

#Herr, Frau, divers
def gendercheck(in_gender):
    if in_gender in t_gender[0:5]:
        return t_Anrede[0]                  #Herr
    elif in_gender in t_gender[5:-2]:
        return t_Anrede[1]                  #Frau
    elif in_gender in t_gender[-2:]:
        return ""                           #divers

#Zeitabhängige Begrüßung
def time_greeting(time):
    if time in t_time[0:10]:
        return t_greetings[0]
    elif time in t_time[10:18]:
        return t_greetings[1]
    elif time in t_time[18:24]:
        return t_greetings[2]

gender, name, time = inputs()
anrede = gendercheck(gender)
greeting = time_greeting(time)
print(f"{greeting}, {anrede} {name}!")




