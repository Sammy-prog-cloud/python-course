my_var1 = 10


def function1():
    global my_var1
    my_var1 = 5
    print(my_var1)


def function2():
    my_var2 = my_var1 * 5
    print(my_var2)


function1()
function2()
