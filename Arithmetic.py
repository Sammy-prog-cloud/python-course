print('''
            Arithmetic values of A and B 
                                                ''')

a = float(input('Please kindly enter the value of a >>> '))
b = float(input('Please kindly enter the value of b >>> '))
addition = a+b
print('The sum of the values ( A and B) is ', addition)
difference = a-b
print('The difference of the values ( A and B) is ', difference)
product = a * b
print('The product of the values ( A and B) is ', product)
quotient = a/b
print('The quotient of the values ( A and B) is ', quotient)
remainder = a % b
print('The remainder of the values ( A and B) is ', remainder)
from math import log10
logarithm_of_a = log10(a)
print('The Logarithm of the values ( A and B) is ', round(logarithm_of_a, 2))
power = a**b
print('The power of the A^B value is ', power)