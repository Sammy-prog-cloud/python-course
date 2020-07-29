initial_velocity = float(input('Enter value for initial_velocity >>> '))
time = float(input('Enter in the time >>> '))
acceleration = 9.8
displacement = initial_velocity * time + (1/2) * (acceleration * time ** 2)
print(round(displacement, 2))