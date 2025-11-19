import random
class Fibo_Generator:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_num = self.first + self.second
        self.first = self.second
        self.second = fib_num
        return fib_num


fib_seq = Fibo_Generator()
for i in range(10):
    print("Fibs : ", next(fib_seq))


print(list(map((lambda x: x * 2), range(1, 11))))
# Another way of writing the above code is below
print([x * 2 for x in range(1, 11)])
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
print([x for x in range(1, 11) if x % 2 != 0])
print([i ** 2 for i in range(50) if i % 8 == 0])
print([x * y for x in range(1, 3) for y in range(11, 16)])
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

multi_list = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
print([col[1] for col in multi_list])
print([multi_list[i][i] for i in range(len(multi_list))])

