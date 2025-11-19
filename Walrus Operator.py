# Walrus Operator is an assignment expression that assigns values to variables as part of a larger expression
# And the symbol is :=

happy = True
print(happy)

print(happy := True)

foods = list()
while food := input("What food do you like ? : ").lower() != "quit":
    foods.append(food)


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)
