print(''' 
                      welcome
            Determining leap year program
                                                '''.upper())
year = int(input('Enter in the year to check for : '))
if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False
# Display result
if isLeapYear:
    print(year, 'Is a Leap Year')
else:
    print(year, 'Is not a Leap Year')