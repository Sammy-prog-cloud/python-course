print('''
                Your Interest for each Year
                                                    '''.upper())
interest = 4/100
deposit = float(input('Kindly input the amount of money deposited >>> '))
amount = deposit+interest
print('Your amount in the savings account after one year is %.2f' % amount)
print('Your amount in the savings account after two years is %.2f' % (2 * amount))
print('Your amount in the savings account after 3 years is %.2f' % (3 * amount))