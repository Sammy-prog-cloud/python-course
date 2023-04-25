loonie = 100
toonie = 200
quarter = 25
dime = 10
nickel = 5
cent = int(input('Enter  the number of cents >>> '))
print(" ", cent // toonie, "toonie")
cent = cent % toonie
print(" ", cent // loonie, "loonie")
cent = cent % loonie
print(" ", cent // dime, "dime")
cent = cent % dime
print(" ", cent // nickel, "nickel")
cent = cent % toonie
