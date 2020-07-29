
def proceed():
    print('''
        1. Call me
        2. Call me back, I love you
        3. Send me Credit
        4. Call me. I have gist for you
        5. Call me. I need your assistance 
    ''')
    choice = int(input())
    if choice == 1:
        print(f"Your Call me has been sent to {number}")
    elif choice == 2:
        print(f"Your Call me back, I love you has been sent to {number}")
    elif choice == 3:
        print(f"Your Send me Credit has been sent to {number}")
    elif choice == 4:
        print(f"Your Call me. I have gist for you has been sent to {number}")
    elif choice == 5:
        print(f"Your Call me. I need your assistance has been sent to {number}")
    else:
        print("Invalid Choice!!!")


print("Welcome to MTN Call Me Back service. Please enter the number ")
print("0xxxxxxxxxx")
number = input()
if number[0] != '0' or len(number) != 11:
    print("The number is not valid!")
else:
    proceed()
