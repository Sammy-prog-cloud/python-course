print('''
            Welcome to the Assessing employees software
                                                        '''.upper())
rating = float(input('Enter in the rating of the employee : '))
employees_raise = rating * 2400.00
meaning = ''
if rating == 0.0:
    meaning = 'Unacceptable Performance'
    print('The Employees rating is', rating, 'indicating', meaning)
    print('The Employees salary is raised by >>> $%.1f ' % employees_raise)
elif rating == 0.4:
    meaning = 'Acceptable Performance'
    print('The Employees rating is', rating, 'indicating', meaning)
    print('The Employees salary is raised by >>> $%.1f ' % employees_raise)
elif rating >= 0.6:
    meaning = 'Meritorious Performance'
    print('The Employees rating is', rating, 'indicating', meaning)
    print('The Employees salary is raised by >>> $%.1f ' % employees_raise)
else:
    print('Invalid Rating !!! Please kindly retry again'.upper())

# rating can not be between 0.0 and 0.4 neither between 0.4 and 0.6
# An employed person is expected to collect 2400 on the rating he / she has in a month