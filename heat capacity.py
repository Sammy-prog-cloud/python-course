print('''
        Solving for Specific heat capacity
                                            '''.upper())
mass = float(input('Type in the mass number >>> '))
temperature_change = float(input('Type in the temperature change >>> '))
specific_heat_capacity = 4.186
total_amount_of_energy = mass * temperature_change * specific_heat_capacity
print('The total amount of energy is %.2f Joules ' % total_amount_of_energy)
electricity_cost = 8.9
cost_heat = total_amount_of_energy / electricity_cost
print(' The cost of heat is  %.2f JoulesC/Kwh ' % cost_heat)
