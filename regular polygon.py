from math import tan, pi
print("""
            Area of a Regular Polygon
                                                            """.upper())
#input section
side = int(input('length of a side >>> '))
number = int(input('Number of sides >>> '))

#output section
area = (number * (side ** 2))/(4 * tan(pi/number))
print('Area of a regular polygon >>> {:.2f} Cm^2 '.format(area))

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
matrix[0][1] = 10
print(matrix[0][1])


number = [0, 1, 2, 4, 5, 5, 6, 7, 8, 6]
uniques = []
for i in number:
    if i not in uniques:
        uniques.append(i)
print(uniques)
