print('''       Bottle deposit          '''.upper())
data = int(input('Number of container of each size  >>>  '))
if data <= 1:
    deposit = 0.10
    refund = deposit * data
    print("Refund >>> ${:.2f}".format(refund))
elif data > 1:
    deposit = 0.25
    refund = deposit * data
    print("Refund >>> ${:.2f}".format(refund))
else:
    print('Invalid data entered !!! ')
print()