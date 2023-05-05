mult_d_list = [[0] * 10 for i in range(10)]
for i in range(10):
    for j in range(10):
        mult_d_list[i][j] = "{} : {}".format(i, j)
for i in range(10):
    for j in range(10):
        print(mult_d_list[i][j], end=" || ")
    print()


number = int(input('Enter in a 4-digit number to add >>> '))
first_number = number // 1000
second_number = (number % 1000) // 100
third_number = (number % 100) // 10
fourth_number = number % 10
sum_1 = first_number + second_number + third_number + fourth_number
print([f"First number =  {first_number}  ", f"Second number =  {second_number}  ",
      f"Third number = {third_number}   ", f"Fourth number = {fourth_number}   "],
      f"SUM = {sum_1} ")
