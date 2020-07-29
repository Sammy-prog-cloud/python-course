height = float(input('What is your height in inches ? >>> '))
weight = float(input('What is your weight in  pounds ? >>> '))
body_mass_index = (weight / (height * height)) * 703
print(body_mass_index)
# otherwise if units are of metres and kilograms, then this should be used
height = float(input('What is your height in metres ? >>> '))
weight = int(input('What is your height in kilograms ? >>> '))
body_mass_index = (weight / (height * height))
print(body_mass_index)