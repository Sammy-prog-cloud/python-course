print('''
        Getting of the first n Positive Integers
                                                    '''. upper())
number = int(input('Please Kindly enter a number >>> '))
if number == 0:
    print('Number can not be Zero!!! Sorry Try again')
else:
    sum_of_integers = (number * (number + 1)) / 2
    print('The sum of the first n positive integers is %.f ' % sum_of_integers)
