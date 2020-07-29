import random
minimum = 1
maximum = 6
roll_again = 'y'
for i in range(1, 6):
    
    dice1 = random.randint(minimum, maximum)
    print(dice1)
    dice2 = random.randint(minimum, maximum)
    print(dice2)