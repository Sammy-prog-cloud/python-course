print('''
            Conversion from Celsius to Kelvin or Fahrenheit
                                                                ''')
temperature = int(input('Enter in the value of the temperature in degree celsius >>>> '))
to_kelvin = 273 + temperature
to_fahrenheit = (9 / 5) * temperature + 32
print('''
        What would you like to convert the temperature to ???
        1. Kelvin
        2. Fahrenheit
                        ''')
selection = int(input('Select an option >>> '))
if selection == 1:
    print(to_kelvin)
elif selection == 2:
    print(to_fahrenheit)
else:
    print('Selection is invalid !!!')