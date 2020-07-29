print('''
        Simple calculator
                                '''.upper())
print('''
        Select Function
        1. Add
        2. Subtract
        3. multiply
        4. Divide
                        ''')
selection = int(input('Select the function you wish to perform '))
number_1 = int(input('Type in number 1: '))
number_2 = int(input('Type in number 2: '))
if selection == 1:
    print('The answer is: ', number_1 + number_2)
elif selection == 2:
    print('The answer is: ', number_1 - number_2)
elif selection == 3:
    print('The answer is: ', number_1 * number_2)
elif selection ==4:
    print('The answer is: ', number_1 / number_2)
else:
    print('Invalid input. Please kindly enter a valid number')




