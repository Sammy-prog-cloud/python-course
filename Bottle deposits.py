less_deposit = 0.10
more_deposit = 0.25
less = int(input('Kindly Enter Number of container for size 1 and below >>> '))
more = int(input('Kindly Number of container for size above 1  >>> '))
refund = less * less_deposit + more * more_deposit
print('Your total refund will be $%.2f.' % refund)