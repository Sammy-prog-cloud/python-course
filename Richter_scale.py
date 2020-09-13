print('Richter scale'.upper())
# the major function of the Richter scale is to know the magnitude of earthquake of a place at the time of the effect
# magnitude needed to be known in other to know the earthquake to go close to and the ones not to

magnitude = float(input('Enter in the magnitude of the earthquake : '))
descriptor = ''
if magnitude < 2.0:
    descriptor = 'Micro'
elif 2.0 < magnitude < 3.0:
    descriptor = 'Very Minor'
elif 3.0 < magnitude < 4.0:
    descriptor = 'Minor'
elif 4.0 < magnitude < 5.0:
    descriptor = 'Light'
elif 5.0 < magnitude < 6.0:
    descriptor = 'Moderate'
elif 6.0 < magnitude < 7.0:
    descriptor = 'Strong'
elif 7.0 < magnitude < 8.0:
    descriptor = 'Major'
elif 8.0 < magnitude < 10.0:
    descriptor = 'Great'
elif magnitude >= 10.0:
    descriptor = 'Meteoric'
print(magnitude, 'signifies', '-----', descriptor, 'Earthquake')