# first_integer = int(input('Enter in a number >>> '))
# second_integer = int(input('Enter in a number >>> '))
# third_integer = int(input('Enter in a number >>>> '))
# fourth_integer = int(input('Enter in a number >>> '))
# summation = first_integer + second_integer + third_integer + fourth_integer
# print(summation)

number = int(input('Enter a four digit number: '))
digit1 = number // 1000
total = number // 100
digit2 = total % 10
digit3 = total % 100
digit4 = number % 10

sum = digit1 + digit2 + digit3 + digit4
print(f"The first is {digit1}, the second is {digit2}, the third is {digit3}, the fourth is {digit4} and sum is {sum}")
