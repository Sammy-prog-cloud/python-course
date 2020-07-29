num_of_subjects = 2
# subject = 2
subjects = []
scores = []

# grade = 5
for i in range(num_of_subjects):
    subject = input("Enter subject {} >>> ".format(i+1))
    subjects.append(subject)
    score = int(input("Enter your score {} >>> ".format(i+1)))
    scores.append(score)

result = """   National Examination Council Result (N.E.C.O)          """


def print_result(subject_name, grade):
    print('|{:<25}|'.format('Subject').upper(), '{:<20}|'.format('Grade').upper())
    print('|{:<25}|'.format(subject_name).upper(), '{:<20}|'.format(grade))
    for j in range(num_of_subjects):
        print('|{:<25}|'.format(subject[j]).upper(), '{:<20}|'.format(grade[j]))
    print()


# print(result.upper())
# for j in range(total_num_of_subjects):
#     print(f"Subject: {subjects[j]}, Score: {scores[j]}")
# print('|{:^25}|'.format('subject').upper(), '{:^20}|'.format('Grade').upper())


if 75 <= score <= 100:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('A1'))
elif 70 <= score < 75:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('B2'))
elif 65 <= score < 70:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('B3'))
elif 60 <= score < 65:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('C4'))
elif 55 <= score < 60:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('C5'))
elif 50 <= score < 55:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('C6'))
elif 45 <= score < 50:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('D7'))
elif 40 <= score < 44:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('E8'))
elif score < 40:
    print('|{:<25}|'.format(subject).upper(), '{:<20}|'.format('F9'))
else:
    print('Wrong entries... Please, check your entry.')