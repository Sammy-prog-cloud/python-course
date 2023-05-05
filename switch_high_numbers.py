import random
number_list = []
for i in range(5):
    number_list.append(random.randrange(1, 9))
for i in number_list:
    print(i, end="")

i = len(number_list) - 1
while i > 1:
    j = 0
    while j < i:
        print('\n Is {} > {} '.format(number_list[j], number_list[j+1]))
        print()
        if number_list[j] > number_list[j+1]:
            print('Switch')
            temp = number_list[j]
            number_list[j] = number_list[j+1]
            number_list[j+1] = temp
        else:
            print("Don't Switch")
        j += 1
        for k in number_list:
            print(k, end="")
        print()
    print("End of Round")
    i -= 1
    for k in number_list:
        print(k, end="")
    print()


my_list = [5, 2, 9, 1]
number = range(5)
print(len(my_list))
print(my_list[0])
print(my_list[0:3])
print(9 in my_list)

print(my_list.insert(0, 10))
print(my_list.sort())
print(my_list.reverse())


