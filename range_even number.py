number = int(input('Enter in a number >>> '))
for i in range(0, 10):
    if i == number:
        # print('Number is even number')
        break
    print(i)
if (number % 2) == 0:
    print('Number is even number')
else:
    print('Number is odd number')