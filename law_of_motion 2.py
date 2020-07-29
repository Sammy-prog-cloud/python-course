initial_velocity = float(input('Initial velocity of object >>> '))
# acceleration = int(input('Acceleration due to gravity >>> '))
acceleration = 9.8
time = float(input('time >>> '))
final_velocity = initial_velocity + (acceleration * time)
print('The final velocity in m >>> ', round(final_velocity, 2), "m/s^2")