print('''   
                        Welcome
      License Plate Validation Check-In Program
                                                '''.upper())
plate = input('Enter in the plate number : ')
if len(plate) == 6 and \
   plate[0].lower() >= "a" and plate[0] <= "z" and \
   plate[1].lower() >= "a" and plate[1] <= "z" and \
   plate[2].lower() >= "a" and plate[2] <= "z" and \
   plate[3] >= "0" and plate[3].lower() <= "9" and \
   plate[4] >= "0" and plate[4].lower() <= "9" and \
   plate[5] >= "0" and plate[5].lower() <= "9":
    print('The plate number is a valid older style plate number')
elif len(plate) == 7 and \
     plate[0].lower() >= "a" and plate[0] <= "z" and \
     plate[1].lower() >= "a" and plate[1] <= "z" and \
     plate[2].lower() >= "a" and plate[2] <= "z" and \
     plate[3] >= "0" and plate[3].lower() <= "9" and \
     plate[4] >= "0" and plate[4].lower() <= "9" and \
     plate[5] >= "0" and plate[5].lower() <= "9" and \
     plate[6] >= "0" and plate[6].lower() <= "9":
    print('The plate number is a valid new style plate number')