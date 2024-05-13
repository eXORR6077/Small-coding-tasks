#AG KW17 

#Rückgeldrechner 

must_pay = float(input("Gib hier deinen Rechnungsbetrag ein\n"))
moneypaid = float(input("Gib hier deinen gezahlten Betrag ein \n"))

if must_pay > moneypaid:
    print(f"Du musst noch {must_pay - moneypaid:.2f}€ bezahlen")
else:
    print(f"Du bekommst {moneypaid - must_pay:.2f}€ zurück")

