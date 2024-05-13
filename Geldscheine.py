#Geldscheine

#zu einem Betrag soll die geringste dafür notwendige Menge an Geldscheinen ermittelt 
#werden: 
#Von der Konsole wird ein Geldbetrag (in Euro ohne Cent, also Ganzzahl) eingelesen. 
#Es gibt Geldscheine mit folgenden Werten: 500, 200, 100, 50, 20, 10, 5 
#Für jeden Wert soll die benötigte Anzahl an Scheinen ausgegeben werden 
#Nur Beträge, die ein Vielfaches von 5 Euro betragen bis maximal 10.000 Euro sind zugelassen 
#Hinweis: 
#mit dem Modulo-Operator % lässt sich der Divisionsrest ermitteln 
#   10 % 5 = 0 10 ist ein erlaubter Betrag 
#   7 % 5 = 2 7 ist kein erlaubter Betrag

banknote_list = [500,200,100,50,20,10,5]
money = int(input("Gimme your money!:\n "))

while money % 5 != 0 or money > 10000:
    input_money = int(input("Invalid operation -> Money needs to be dividable by 5 and can not be more than 10000€ - Gimme your money!\n: "))
    money = input_money
else:    
    for banknote in banknote_list:
        anzahl = money // banknote
        money %= banknote
        print(f"{anzahl} x {banknote}€-Note")


