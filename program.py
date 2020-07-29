all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
login = 'sammyDen'
password = input('Enter the password >>> ')
if login == 'sammyDen':
    print('Welcome')
elif login:
    print('Sorry! you'+'ve' 'entered an incorrect password')
status = bool(input('OK to proceed >>> '))
print(status)
print(type(status))


