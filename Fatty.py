number = int(input('Enter a number:  '))
from math import factorial
solution = factorial(number)
print(solution)

print('''Calculating factorial of a number'''.upper())
number = int(input('Type in a number: ').isnumeric())
from math import factorial
for i in range(number, (number - 1)):
    if number < 0:
        print('Invalid input, check and try again !!! ')
    elif number == number:
