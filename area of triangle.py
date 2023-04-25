from math import sqrt
print('''
            Area of triangle using s1, s2, s3
                                                                '''.upper())

#data to be entered in this section
length_1 = int(input('Enter in the length of the first side (L1) >>> '))
length_2 = int(input('Enter in the length of the second side (L2) >>> '))
length_3 = int(input('Enter in the length of the third side (L3) >>> '))

#data computed
total_length = (length_1 + length_2 + length_3) / 2
area_triangle = sqrt(total_length * (total_length - length_1) * (total_length - length_2) * (total_length - length_3))

#data output
print('The area of the triangle >>> {:.2f} '.format(area_triangle))
