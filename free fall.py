from math import sqrt
height = float(input('Enter in the height in metres >>> '))
initial_speed = 0
acceleration_gravity = 9.8
final_speed = sqrt((initial_speed**2) + (2 * acceleration_gravity * height))
print('Final speed >>> {:.2f} m/s'.format(final_speed))