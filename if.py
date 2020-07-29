number = int(input('Enter a number >>> '))
if number < -1:
    print("Number is negative")
elif number == 0:
    print('Number is also positive')
elif number == -1:
    print('I would love to get a pie')
else:
    print('Number is positive')
if (number % 2) == 0:
    print('Its an even number')
else:
    print('Its an odd number')
while number <= 10:
    print('{}'.format(number), end=" ")
    number += 1