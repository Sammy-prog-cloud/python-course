print('''
        Welcome to the letter grading program
                                                '''.upper())
letter_grade = str(input('Enter in the letter grade : '))
if letter_grade.upper() == "A+":
    print('Grade point >>>> ', 4.0)
elif letter_grade.upper() == "A":
    print('Grade point >>> ', 4.0)
elif letter_grade.upper() == "A-":
    print('Grade point >>>> ', 3.7)
elif letter_grade.upper() == "B+":
    print('Grade point >>>> ', 3.3)
elif letter_grade.upper() == "B":
    print('Grade point >>>> ', 3.0)
elif letter_grade.upper() == "B-":
    print('Grade point >>>> ', 2.7)
elif letter_grade.upper() == "C+":
    print('Grade point >>>> ', 2.3)
elif letter_grade.upper() == "C":
    print('Grade point >>>> ', 2.0)
elif letter_grade.upper() == "C-":
    print('Grade point >>>> ', 1.7)
elif letter_grade.upper() == "D+":
    print('Grade point >>>> ', 1.3)
elif letter_grade.upper() == "D":
    print('Grade point >>>> ', 1.0)
elif letter_grade.upper() == "F":
    print('Grade point >>>> ', 0)
else:
    print('Invalid letter Grade')