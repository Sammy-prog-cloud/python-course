# selling_price = 3.49
# discount = (60 / 100) * 3.49
# number_bread = int(input('Enter the number of loaves of day old bread: '))
# print('The selling price of bread is $%5.2f' % selling_price)
# price = number_bread * discount
# print('The discount on a day old bread $%5.2f' % discount)
# print('The total price of bread bought bought is $%5.2f' % price)
bread_price = 3.49
discount_rate = 0.60
num_loaves = int(input('Enter the number of day old loaves : '))
regular_price = num_loaves * bread_price
discount = regular_price * discount_rate
total = regular_price - discount
print('Regular price : %5.2f' % regular_price)
print('Discount : %5.2f' % discount)
print('Total : %5.2f' % total)
