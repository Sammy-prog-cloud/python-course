
def selection():
    print('''
        1. Migrate to MTN pulse
        2. 1.5GB @ N500(Pulse ONLY)
        3. Music+ @  N10
        4. NightLife Bundles
        5. InstaBinge Bundles
        6. GoodyBag
        7. 750MB @  N300 (Pulse ONLY)
        ''')
    choice = int(input())
    if choice == 1:
        print('Do you wish to migrate???')
        print('''
            1. Proceed
            0. Back
            ''')
        input()
        print("Y'ello You have successfully migrated to MTN Pulse")
    elif choice == 2:
        print('You will be charged N500 for this bundle, Valid for 7days')
        print('''
            1. Proceed
            0. Back
            ''')
        choice_2 = int(input())
        if choice_2 == 1:
            print('Do you want your Pulse DataPlan 1.5GB to automatically renew every 7days?')
            print('''
            1. Yes (Auto-Renew)
            2. No (One-off)''')
            yes = int(input())
            if yes == 1:
                print("Y'ello you have successfully subscribed and Renews after 7days")
            elif yes == 2:
                print('One-off subscription to MTN Pulse 1.5GB enabled')
            else:
                print('bye')
    elif choice == 3:
        print('You will be charged N10 and service will be renewed daily')
        print('''
        1. Proceed
        0. Back''')
        music = int(input())
        if music == 1:
            print('You have successfully subscribed to Music+')
        else:
            print('Invalid entry!!!')
    elif choice == 4:
        print('Enjoy Pulse Nightlife browsing from 12am - 5am (Fair usage policy of 500MB applies)')
        print('''
            1. 250MB Pulse Nightlife @ N25
            2. 500MB Pulse Nightlife @ N50
            3. Balance''')
        choose = int(input())
        if choose == 1:
            print('You will be charged 250MB for N25 Pulse Nightlife Bundle')
            print('''
                1. Confirm
                0. Back''')
            process = int(input())
            if process == 1:
                print('You have successfully subscribed to N25 for 250MB MTN Nightlife')
            else:
                print('error!!!')
        if choose == 2:
            print('You will be charged N50 for the purchase of 500MB MTN Pulse Nightlife Bundle')
            print('''
                1. confirm
                0. Back''')
            option = int(input())
            if option == 1:
                print('You have successfully subscribed to N50 for 500MB MTN Pulse Nightlife Bundle')
            else:
                print('Invalid!!!')
        elif choose == 3:
            print('Your MTN Pulse Nightlife balance is ..... ')


print("Y'ello Welcome to MTN Pulse migration")
selection()

