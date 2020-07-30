number_of_sides = int(input('Enter in the number of sides the shape has : '))
if number_of_sides == 3:
    print("It's a Triangle")
elif number_of_sides == 4:
    print("It's a Quadrilateral")
elif number_of_sides == 5:
    print("It's a Pentagon")
elif number_of_sides == 6:
    print("It's a Hexagon")
elif number_of_sides == 7:
    print("It's a Heptagon")
elif number_of_sides == 8:
    print("It's an Octagon")
elif number_of_sides == 9:
    print("It's a Nonagon")
elif number_of_sides == 10:
    print("It's a Decagon")
elif number_of_sides < 3 or number_of_sides > 10:
    print('Invalid input!!! check and re-enter your value')
else:
    print()