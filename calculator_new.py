from math import log


def calculator():
    print('''Choose a function to perform: 
                        1. Addition
                        2. Subtraction
                        3. Division
                        4. Multiplication
                        5. Square of the two numbers
                        6. Cube of the two numbers
                        7. Logarithm of such number
                                                    ''')
    selection = int(input('Choose an option: '))
    if selection < 1 or selection > 7:
        print('Invalid number')
        return
    number = int(input('Enter in first number : '))
    number_2 = int(input('Enter in the second number : '))
    if selection == 1:
        print(number + number_2)
    elif number == 2:
        print(number - number_2)
    elif selection == 3:
        print(number / number_2)
    elif selection == 4:
        print(number * number_2)
    elif selection == 5:
        print(number ** 2, number_2 ** 2)
    elif selection == 6:
        print(number ** 3, number_2 ** 3)
    elif selection == 7:
        print(log(number, number_2))
    else:
        print('end')


calculator()
