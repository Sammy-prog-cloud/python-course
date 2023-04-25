# Take in input from the user
pressure = float(input('Enter in the pressure (in pascals) >>> '))
volume = float(input('Enter in the volume >>> '))
temp = int(input('Enter in the temperature  (In celsius) >>> '))
# Define constants
ideal_constant = 8.314
temperature_constant = 273
# Compute the constants
total_temp = temperature_constant + temp
number_moles = pressure * volume / ideal_constant * total_temp
print('Number in moles >>> {:.2f} moles'.format(number_moles))
