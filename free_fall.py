z = ''' 
                Free fall 
                                        '''
print(z)
from math import sqrt
height = int(input('Enter in the height in metres: '))
acceleration_due_to_gravity = 9.8
initial_speed = 0
final_speed = sqrt((initial_speed ** 2) + 2 * acceleration_due_to_gravity * height)
print('The final speed is %.f m/s^2 ' % final_speed)