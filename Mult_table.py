# This below is a 2D list of numbers
# mult_table = [[0] * 10 for i in range(10)]
# # It outputs a list of 10 in ten separate list i.e. [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] * 10
# for i in range(1, 10):
#     for j in range(1, 10):
#         mult_table[i][j] = i * j
#
# for i in range(1, 0):
#     for j in range(1, 10):
#         print(mult_table[i][j], end=" ")
#     print()

customers = []
while True:
    create_entry = input("Enter customer (Yes / No) : ").lower()
    if create_entry == "y":
        f_name, l_name = input('Enter in customer name : ').split()
        customers.append({"f_name": f_name, "l_name": l_name})
    else:
        break

for cust in customers:
    print(cust['f_name'], cust['l_name'])


# def fibo(num):
#
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         result = fibo(num-1) + fibo(num-2)
#         return result
#
#
# number = int(input("How many Fibonacci values should be found? : "))
# i = 1
# while i <= number:
#     fib_value = fibo(i)
#     print(fib_value)
#     i += 1
#
# print("\nFinal Answer : ", fibo(number))






