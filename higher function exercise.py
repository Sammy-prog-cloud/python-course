z = '''
            welcome to the higher function
                                            '''
print(z)


def my_higher_order_function(i, triple):
    if i == triple:
        return i * i * i
    triple()


print(my_higher_order_function(3, triple=3))
# print(my_higher_order_function(2, double=2))