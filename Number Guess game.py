print('''
            Guess a number Game
                                    '''.upper())
import random
number_to_guess = random.randint(1, 10)
guess = int(input('Enter a number between 1 and 10  >>> '))
while number_to_guess != guess:
    print('Wrong number')
    guess = int(input('Guess again >>> '))
    count_number_of_tries = 1
    if count_number_of_tries == 4:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')
    guess = int(input('Please guess again: '))
    count_number_of_tries += 1
    if number_to_guess == guess:
        print('Well done You Won')
        print('It took you', count_number_of_tries, 'goes to complete the game')
        print('Congratulations')
    else:
        print('Sorry you lose !!!')
        print('The number you needed to guess was', number_to_guess)
    print(''' 
            Do you wish to play again ???   
                    1. yes
                    2. No
                    ''')
    answer = int(input())
    number_to_guess = random.randint(1, 10)
    guess = int(input('Enter a number between 1 and 10  >>> '))
    if answer == 1:
        while number_to_guess != guess:
            print('Wrong number')
            guess = int(input('Guess again >>> '))
            count_number_of_tries = 1
            if count_number_of_tries == 4:
                break
            elif guess < number_to_guess:
                print('Your guess was lower than the number')
            else:
                print('Your guess was higher than the number')
            guess = int(input('Please guess again: '))
            count_number_of_tries += 1
            if number_to_guess == guess:
                print('Well done You Won')
                print('It took you', count_number_of_tries, 'goes to complete the game')
                print('Congratulations')
            else:
                print('Sorry you lose !!!')
                print('The number you needed to guess was', number_to_guess)
    else:
        print('Bye')
    print('Game Over')
