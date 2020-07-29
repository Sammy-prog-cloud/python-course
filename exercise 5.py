total_num_of_courses = 5
sum_of_scores = 0

for i in range(total_num_of_courses):
    scores = int(input("score of course {}".format(i+1)))
    sum_of_scores += scores

average = sum_of_scores / total_num_of_courses

print("the sum of the score is {} and the average is {}".format(sum_of_scores, average))
