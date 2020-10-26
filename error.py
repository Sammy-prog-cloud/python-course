try:
    birth_year = int(input('Enter in the birth year : '))
    age = 2019 - birth_year
    income = 20000
    risk = income / birth_year
    print(age)
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('Invalid Input or Number')