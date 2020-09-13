# year = int(input('Enter in the year : '))
# animal = ""
# if year == 2000:
#     animal = "Dragon"
# elif year == 2001:
#     animal = "Snake"
# elif year == 2002:
#     animal = "Horse"
# elif year == 2003:
#     animal = "Sheep"
# elif year == 2004:
#     animal = "Monkey"
# elif year == 2005:
#     animal = "Rooster"
# elif year == 2006:
#     animal = "Dog"
# elif year == 2007:
#     animal = "Pig"
# elif year == 2008:
#     animal = "Rat"
# elif year == 2009:
#     animal = "Ox"
# elif year == 2010:
#     animal = "Tiger"
# elif year == 2011:
#     animal = "Hare"
# print(year, '-----', animal)
# The above one is for the year directly while the down part is for modulo
year = int(input('Enter in the year : '))
animal = ""
if year % 12 == 8:
    animal = "Dragon"
elif year % 12 == 9:
    animal = "Snake"
elif year % 12 == 10:
    animal = "Horse"
elif year % 12 == 11:
    animal = "Sheep"
elif year % 12 == 0:
    animal = "Monkey"
elif year % 12 == 1:
    animal = "Rooster"
elif year % 12 == 2:
    animal = "Dog"
elif year % 12 == 3:
    animal = "Pig"
elif year % 12 == 4:
    animal = "Rat"
elif year % 12 == 5:
    animal = "Ox"
elif year % 12 == 6:
    animal = "Tiger"
elif year % 12 == 7:
    animal = "Hare"
print("%d is the year of the %s." % (year, animal))