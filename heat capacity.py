spec_heat_capacity = 4.186
mass = int(input('Enter in the mass >>> '))
temp_1 = int(input('Enter in T1 >>> '))
temp_2 = int(input('Enter int T2 >>> '))
temp_change = temp_2 - temp_1
standard_mass = 1.0 * mass
total_energy = standard_mass * spec_heat_capacity * temp_change
print('Total energy >>> {:.2f} Joules'.format(total_energy))
