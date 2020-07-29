def choice():
    print('Enjoy access to Instagram with Pulse. InstaBinge bundles')
    print('''
        1. Instagram 250MB @ N100
        2. Instagram 1GB @ N200
        3. Check Balance''')
    insta = int(input())
    if insta == 1:
        print('''
            1. Proceed with purchase of 250MB @ N100. Valid for 1 day
            2. Opt-in for Auto-Renewal
            3. Cancel Auto-Renewal
            0. Back''')
        purchase = int(input())
        if purchase == 1:
            print('You have successfully subscribed to Instagram 250MB @ N100 Bundle')
        elif purchase == 2:
            print('Do you wish to opt-in for Auto-Renewal of 250MB Pulse InstaBinge Lite bundle')
            print('''
                1. Proceed
                0. Back ''')
            binge = int(input())
            if binge == 1:
                print("Y'ello you have successfully subscribed to Instagram 250MB @ N100 Bundle. Auto-Renewal enabled")
            else:
                print('Bye')
        elif purchase == 3:
            print('Auto-Renewal disabled')
        else:
            print('bye')
    elif insta == 2:
        print('''
                1. Proceed with purchase of 1GB @ N200. Valid for 1 day
                2. Opt-in for Auto-Renewal
                3. Cancel Auto-Renewal
                0. Back''')
        renewal = int(input())
        if renewal == 1:
            print('You have successfully subscribed to 1GB @ N200 Instagram Bundle')
        elif renewal == 2:
            print('Auto-Renewal enabled')
        elif renewal == 3:
            print('Auto-Renewal disabled')
        else:
            print('Bye')
    elif insta == 3:
        print("Y'ello your InstaBinge Data Balance is :  ")
    else:
        print('Bye')