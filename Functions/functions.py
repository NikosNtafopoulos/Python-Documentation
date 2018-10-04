def first_function(message):
    return 'The message of the function is {}'.format(message)


print first_function(
    '[Tip of the day: You can make a function with and without arguments]')


# function with default argument
def hello_func(greeting, name="There"):
    return '{}, {}'.format(greeting, name)


# passing only the first argument and still working because of name="There" --> passing argument with default value
print(hello_func('Hello'))


def calculations(num1, num2):
    result = num1 + num2
    return 'and the result is: ' + str(result)


print calculations(5, 5)


def student_info(*args, **kwargs):
    # printing as tuples
    print(args)
    # printing as dictionary
    print(kwargs)


student_info('Math', 'Chemistry', name='Nik', age="27")
