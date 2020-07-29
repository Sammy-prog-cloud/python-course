def process():
    print('''
        1. Risky by Davido
        2. Blow My Mind by Davido
        3. 1 Milli by Davido
        4. Hot Tunez
        98. More ''')
    proceed = int(input())
    if proceed == 1:
        print('Do you wish to subscribe to the Risky by Davido CallerTUnez')
        print('''
                    1. Yes 
                    2. No''')
        inter = int(input())
        if inter == 1:
            print('You have successfully subscribed to Risky by Davido CallerTunez')
        elif inter == 2:
            print('Bye')
        else:
            print('Invalid response')
    if proceed == 2:
        print("Do you wish to subscribe to Blow My Mind by Davido CallerTunez??")
        print('''
            1. Yes 
            2. No''')
        inter = int(input())
        if inter == 1:
            print('You have successfully subscribed to Blow my Mind by Davido CallerTunez')
        elif inter == 2:
            print('Bye')
        else:
            print('Invalid response')
    if proceed == 3:
        print("Do you wish to subscribe to 1 Milli by Davido CallerTunez??")
        print('''
                    1. Yes 
                    2. No''')
        inter = int(input())
        if inter == 1:
            print('You have successfully subscribed to Milli by Davido CallerTunez')
        elif inter == 2:
            print('Bye')
        else:
            print('Invalid response')


print("""Y'ello!!!  Welcome to MTN CallerTunez.
        """)
process()