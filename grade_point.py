print('''
            Welcome to the grade point program
                                                '''.upper())
grade_point = float(input('Enter in the grade point : '))
letter_grade = " "
if grade_point > 4.0:
    letter_grade = "A+"
elif grade_point == 4.0:
    letter_grade = "A"
elif 3.7 <= grade_point < 4.0:
    letter_grade = "A-"
elif 3.3 <= grade_point == 3.7:
    letter_grade = "B+"
elif 3.0 <= grade_point < 3.3:
    letter_grade = "B"
elif 2.7 <= grade_point < 3.0:
    letter_grade = "B-"
elif 2.3 <= grade_point < 2.7:
    letter_grade = "C+"
elif 2.0 <= grade_point < 2.3:
    letter_grade = "C"
elif 1.7 <= grade_point < 2.0:
    letter_grade = "C-"
elif 1.3 <= grade_point < 1.7:
    letter_grade = "D+"
elif 1.0 <= grade_point < 1.3:
    letter_grade = "D"
elif 0 <= grade_point < 1.0:
    letter_grade = "F"
else:
    print('Invalid grade point'.upper())
print('The grade point', grade_point, 'is equivalent to', letter_grade)