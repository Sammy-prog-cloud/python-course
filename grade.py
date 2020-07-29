subject = input("Enter subject >>> ")
mark = int(input("Enter your mark >>> "))
result = "   National Examination Council Result (N.E.C.O)      "


def print_result(subject_name, grade):
    print(result.upper())
    print('|{:<25}|'.format('Subject').upper(), '{:<20}|'.format('Grade').upper())
    print('|{:<25}|'.format(subject_name).upper(), '{:<20}|'.format(grade))


# print('|{:<25}|'.format('Subject').upper())
if 75 <= mark <= 100:
    print_result(subject, 'A1')
    # print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('A1'))
elif 70 <= mark < 75:
    print_result(subject, 'B2')
elif 65 <= mark < 70:
    print_result(subject, 'B3')
elif 60 <= mark < 65:
    print_result(subject, 'C4')
elif 55 <= mark < 60:
    print_result(subject, 'C5')
elif 50 <= mark < 55:
    print_result(subject, 'C6')
elif 45 <= mark < 50:
    print_result(subject, 'D7')
elif 40 <= mark < 44:
    print_result(subject, 'E8')
elif mark < 40:
    print_result(subject, 'F9')
else:
    print('Wrong entries... Please, check your entry.')

