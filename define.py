age = int(input('Please input your age: '))
print('age is', age.__doc__)


def greeter(name,
            title='Dr',
            prompt='Welcome',
            message='Live Long and Prosper'):
    print(prompt, title, name, '-', message)


greeter(message='We like Python', name='Lloyd')
