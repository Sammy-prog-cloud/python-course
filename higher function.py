def get_msg():
    return 'Python World !!!'


message = get_msg()
print(message)
print(type(get_msg))
another_reference = get_msg()
print(another_reference)

print('=' * 45)


def get_some_other_msg():
    return 'Some Other Message'


get_msg = get_some_other_msg()
print(get_msg)
print(another_reference)

print('=' * 50)


def apply(x, function):
    result = function(x)
    return result

