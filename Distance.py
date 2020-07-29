from math import acos, radians, sin, cos
'''Latitude'''
t1 = radians(int(input('enter in the value of t1:  ')))
t2 = radians(int(input('Enter in the value of t2:  ')))

'''Longitude'''
g1 = radians(int(input('Enter in the value of g1:  ')))
g2 = radians(int(input('Enter in the value of g2:  ')))

distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
print('The distance between two points on earth is %.2f Km' % distance)