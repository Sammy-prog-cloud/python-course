# The only issue with this 1st method is that the month has to be entered exactly the way it is in the codes !!!!!!!

month = input('Enter in the name of the month : ')
if month == "January" or month == "March" or \
   month == "May" or month == "July" or \
   month == "August" or month == "October" or \
   month == "December":
    print(month.upper(), 'has 31 days')
elif month == "November" or month == "September" or \
     month == "April" or month == "June":
    print(month.upper(), 'has 30 days')
elif month == "February":
    print(month.upper(), 'has 28 or 29 days')

    # another way to do it is this
    # there are so many ways to solving issues in python
    # though i really love the other method below
    # Wow !!! But i know these are not the only way to solve them though.


month = input('Enter the name of the month : ').upper()
days = 31
if month == "April" or month == "November" or \
   month == "June" or month == "September":
    days = 30
elif month == "February":
    days = "28 or 29"
print(month, "has", days, "days in it.")


