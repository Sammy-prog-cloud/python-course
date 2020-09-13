length_1 = int(input('length of the first side of triangle : '))
length_2 = int(input('length of the second side of triangle : '))
length_3 = int(input('length of the third side of triangle : '))
if length_1 == length_2 or length_2 == length_3 or \
   length_3 == length_1:
    print('Its an Isosceles triangle')
elif length_1 == length_2 or length_2 == length_3:
    print('Its an Equilateral triangle')
else:
    print('Its a Scalene triangle')