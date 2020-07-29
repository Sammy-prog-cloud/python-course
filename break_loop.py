print('Only print if all iterations completed'.upper())
number = int(input('Enter a number to check for >>> '))
for i in range(0, 6):
    if i == number:
        break
    print(i, ' ', end='')
print()
print('Done')
