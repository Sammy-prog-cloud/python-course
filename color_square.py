print('''
        Colors on checker board
                                    '''.upper())
letter = input('Enter in the Letter : '.upper())
number = int(input('Enter in the number of the position : '))
if number > 8 or number < 1:
    print('Invalid number')
elif letter.lower() == 'a' and number % 2 == 1:
    print('The Color is Black'.upper())
elif letter.lower() == 'b' and number % 2 == 0:
    print('The Color is Black'.upper())
elif letter.lower() == 'c' and number % 2 == 1:
    print('The Color is Black'.upper())
elif letter.lower() == 'd' and number % 2 == 0:
    print('The Color is Black'.upper())
elif letter.lower() == 'e' and number % 2 == 1:
    print('The Color is Black'.upper())
elif letter.lower() == 'f' and number % 2 == 0:
    print('The Color is Black'.upper())
elif letter.lower() == 'g' and number % 2 == 1:
    print('The Color is Black'.upper())
elif letter.lower() == 'h' and number % 2 == 0:
    print('The Color is Black'.upper())
elif letter == 'i' or 'j' or 'k' or 'l' 'm' or \
     'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or \
     'u' or 'v' or 'w' or 'x' or 'y' or 'z':
    print('Invalid Letter')
else:
    print('The Color is White'.upper())