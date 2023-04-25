customer = {
    'name': 'Yi-Lun',
    'age': 18,
    'email': 'Samxden99@gmail.com',
    "is_verified": True
}
print(customer.get('email'))

print('''
            Phone number in words 
                                                        '''.upper())
phone = input('Phone >>> ')
number = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
output = ""
for item in phone:
    output += number.get(item, '!') + " "
print(output.upper())
