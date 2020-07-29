volume = int(input('Enter in the volume in litres >>> '))
pressure = int(input('Enter in the pressure in Pascal >>> '))
ideal_gas_constant = 8.314
temperature = int(input('Enter in the temperature in celsius >>> '))
temperature_in_kelvin = temperature + 273
n = (pressure * volume) / (ideal_gas_constant * temperature_in_kelvin)
print('The Amount of gas in moles is %.2f moles' % n)
