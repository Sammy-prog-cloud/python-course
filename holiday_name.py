month = input('Enter in the month : ')
day = int(input('Enter in the day of the month : '))
if month == "January".lower() and day == 1:
    print("It's New Year's Day !!!")
elif month == "July".lower() and day == 1:
    print("It's Canada Day !!!")
elif month == "December".lower() and day == 25:
    print("It's Christmas Day !!!")
else:
    print("Entered Month and Day do not correspond")
