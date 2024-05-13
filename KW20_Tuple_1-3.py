#KW20_Tuple

#1. Tupel erstellen und ausgeben
#   es ist ein Tupel mit 5 Obstsorten (Datentyp str) zu erstellen und auf der Konsole auszugeben

fruits = ("pineapple", "apple", "banana", "strawberry", "blueberry")

#2. weitere Tupel
#   zwei weitere Tupel sind zu erstellen, das eine enthält 4 Milchprodukte und einem leeren
#   String, das andere 2 Backwaren. Beide Tupel sind auf der Konsole nacheinander auszugeben.

milk_products = ("milk", "chocolate_milk", "chocolate_bar", "icecream","")

bakery = ("croissant", "cake")

print(milk_products, bakery)

#3. mehrere Tupel zusammenfügen
#   alle 3 Tupel sind in einem neuen Tupel zusammenzufügen. Auf der Konsole ist das Tupel
#   selbst, sowie der Datentyp des Tupels (Hinweis: type() ) auszugeben. Weiterhin sind das erste
#   und das letzte Element des Tupels sowie deren Typ auszugeben

tuple_sum = fruits + milk_products + bakery

print(f"Das gesamte Tupel:{tuple_sum}\nhat Datentyp: {type(tuple_sum)}\nDas erste Element: {tuple_sum[0]} hat Datentyp: {type(tuple_sum[0])}\nDas letzte Element: {tuple_sum[-1]} hat Datentyp: {type(tuple_sum[-1])}")




