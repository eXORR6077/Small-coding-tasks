#Rabattrechner

payed_price = float(input("Gib deinen bezahlten Preis ein:\n"))
disc_perc = float(input("Gib hier deinen Rabatt(in %) ein:\n"))

full_price = (payed_price/(100 - disc_perc))*100
money_saved = ((payed_price/(100 - disc_perc))*100) - payed_price


if payed_price > full_price:
    print("Discount is not valid!")
else:
    print(f"Your discount granted is {disc_perc}% and you saved {money_saved:.2f}€\nThe full price without discount was {full_price:.2f}€")