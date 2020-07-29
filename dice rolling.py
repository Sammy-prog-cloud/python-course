print('''
                Ludo Game 
                                '''.upper())
import random
minimum = 1
maximum = 6
roll_again = 'y'
while roll_again == 'y':
    print('Rolling Dice .... ')
    print('The values are .... ')
    dice1 = random.randint(minimum, maximum)
    print(dice1)
    dice2 = random.randint(minimum, maximum)
    print(dice2)
    roll_again = input('Roll the dice again? (y for yes/ n for no): ').lower()
