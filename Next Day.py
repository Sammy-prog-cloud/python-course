print('''
                     Welcome
         Determination of Next Day Program
                                             ''')
day = int(input('Enter in the day : '))
month = int(input('Enter in the month : '))
year = int(input('Enter in the year : '))
if 1 <= day <= 31 and month == 1:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 29 and month == 2:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 31 and month == 3:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 30 and month == 4:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 31 and month == 5:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 30 and month == 6:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 31 and month == 7:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 31 and month == 8:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 30 and month == 9:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 31 and month == 10:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 30 and month == 11:
    print('The next date is ', day + 1, '-', month, '-', year)
elif 1 <= day <= 31 and month == 12:
    print('The next date is ', day + 1, '-', month, '-', year)
else:
    print('Kindly Enter in a Valid Date')