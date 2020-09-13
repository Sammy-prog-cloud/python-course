month = input('Enter in the month of birth : ')
day = int(input('Enter in the day of birth : '))
# The name of the sign signifies the Astrological sign of the month people are given birth to !!!
if month.lower() == "december" and 21 < day <= 31:
    print(month.upper(), day, '-----', "Capricorn Sign".upper())
elif month.lower() == "january" and 0 < day <= 19:
    print(month.upper(), day, '-----', "Capricorn Sign".upper())
elif month.lower() == "january" and 19 < day <= 31:
    print(month.upper(), day, '-----', "Aquarius Sign".upper())
elif month.lower() == "february" and 0 < day <= 18:
    print(month.upper(), day, '-----', "Aquarius Sign".upper())
elif month.lower() == "february" and 18 < day >= 29:
    print(month.upper(), day, '-----', "Pisces Sign".upper())
elif month.lower() == "march" and 0 < day <= 20:
    print(month.upper(), day, '-----', "Pisces Sign".upper())
elif month.lower() == "march" and 20 < day <= 31:
    print(month.upper(), day, '-----', "Aries Sign".upper())
elif month.lower() == "april" and 0 < day <= 19:
    print(month.upper(), day, '-----', "Aries Sign".upper())
elif month.lower() == "april" and 19 < day <= 30:
    print(month.upper(), day, '-----', "Taurus Sign".upper())
elif month.lower() == "may" and 0 < day <= 20:
    print(month.upper(), day, '-----', "Taurus Sign".upper())
elif month.lower() == "may" and 20 < day <= 31:
    print(month.upper(), day, '-----', "Gemini Sign".upper())
elif month.lower() == "june" and 0 < day <= 20:
    print(month.upper(), day, '-----', "Gemini Sign".upper())
elif month.lower() == "june" and 20 < day <= 30:
    print(month.upper(), day, '-----', "Cancer Sign".upper())
elif month.lower() == "july" and 0 < day <= 22:
    print(month.upper(), day, '-----', "Cancer Sign".upper())
elif month.lower() == "july" and 22 < day <= 31:
    print(month.upper(), day, '-----', "Leo Sign".upper())
elif month.lower() == "august" and 0 < day <= 22:
    print(month.upper(), day, '-----', "Leo Sign".upper())
elif month.lower() == "august" and 22 < day <= 31:
    print(month.upper(), day, '-----', "Virgo Sign".upper())
elif month.lower() == "september" and 0 < day <= 22:
    print(month.upper(), day, '-----', "Virgo Sign".upper())
elif month.lower() == "september" and 22 < day <= 30:
    print(month.upper(), day, '-----', "Libra Sign".upper())
elif month.lower() == "october" and 0 < day <= 22:
    print(month.upper(), day, '-----', "Libra Sign".upper())
elif month.lower() == "october" and 22 < day <= 31:
    print(month.upper(), day, '-----', "Scorpio Sign".upper())
elif month.lower() == "november" and 0 < day <= 21:
    print(month.upper(), day, '-----', "Scorpio Sign".upper())
elif month.lower() == "november" and 21 < day <= 30:
    print(month.upper(), day, '-----', "Sagittarius Sign".upper())
elif month.lower() == "december" and 0 < day <= 21:
    print(month.upper(), day, '-----', "Sagittarius Sign".upper())
else:
    print('Invalid input')




