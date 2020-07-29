print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for z in range(0, 6):
    if z == num:
        break
    print(z, ' ', end='')
else:
    print()
    print('All iterations successful')