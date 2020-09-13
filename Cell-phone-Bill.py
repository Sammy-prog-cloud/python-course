print('''
               welcome !!!
        cell phone bill program
                                '''.upper())
number_minute = int(input('Enter in the number of minute : '))
text_message = int(input('Enter in the number of text messages : '))
minute_message = 15.00
support_911 = 0.44
#
if number_minute > 50 and text_message > 50:
    additional_minute = int(input('Enter in additional minute if any >>> '))
    answer_minute = additional_minute * 0.25
    additional_message = int(input('Enter in additional text message if any >>> '))
    answer_message = additional_message * 0.15
    sales_tax = (minute_message + answer_minute + answer_message + support_911) * (5 / 100)
    total_cost = minute_message + answer_minute + answer_message + support_911 + sales_tax
    print('The base charge  : $%.2f' % minute_message)
    print('The additional message charges : $%.2f' % answer_message)
    print('The additional minute charges : $%.2f' % answer_minute)
    print('The tax : $%.2f ' % sales_tax)
    print('The Total Charge : $%.2f ' % total_cost)

elif number_minute <= 50 and text_message <= 50:
    sales_tax = (minute_message + support_911) * (5 / 100)
    total_cost = minute_message + support_911 + sales_tax
    print('The base charge  : $%.2f' % minute_message)
    print('The tax : $%.2f : ' % sales_tax)
    print('The Total Charge : $%.2f ' % total_cost)
else:
    print('Invalid Input')
