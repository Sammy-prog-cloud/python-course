naMe = input("Enter in a name : ").upper()
name = ""
for char in naMe:
    name += str(ord(char))
print("Secret Message : ", name)
naMe = ""
for i in range(0, len(name) - 1, 2):
    char_code = name[i] + name[i + 1]
    naMe += chr(int(char_code))
print("Original Message : ", naMe)

naMe = input("Enter in a name : ").upper()
name = ""
for char in naMe:
    name += str(ord(char))
print("Secret Message : ", name)
naMe = ""
for i in range(0, len(name) - 1, 1):
    char_code = name[i] + name[i + 1]
    naMe += chr(int(char_code))
print("Original Message : ", naMe)
