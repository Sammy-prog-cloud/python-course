# final_velocity = 'final velocity of object'
initial_velocity = float(input('Initial velocity of object >>> '))
acceleration = 9.8
displacement = float(input('Displacement of object >>> '))
final_velocity = initial_velocity + 2 * (acceleration * displacement)
print('The final velocity >>> ', round(final_velocity, 2), 'm/s^2')