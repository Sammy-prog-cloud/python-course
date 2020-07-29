total_num_of_courses = 5
sum_of_courses = 0

for i in range(total_num_of_courses):
    score = int(input("Enter the score in course {} >>> ".format(i+1)))
    sum_of_courses += score

average = sum_of_courses / total_num_of_courses

print("The sum of the scores is {} and the average is {}".format(sum_of_courses, average))
