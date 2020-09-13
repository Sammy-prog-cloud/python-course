denomination = int(input('Enter in a denomination of money : '))
name = ''
if denomination == 1:
    name = 'George Washington'
elif denomination == 2:
    name = 'Thomas Jefferson'
elif denomination == 5:
    name = 'Abraham Lincoln'
elif denomination == 10:
    name = 'Alexander Hamilton'
elif denomination == 20:
    name = 'Andrew Jackson'
elif denomination == 50:
    name = 'Ulysses S. Grant'
elif denomination == 100:
    name = 'Benjamin Franklin'
else:
    print('You have entered an invalid denomination of money')
print('Sir', name, 'is on the face of $%.f' % denomination)