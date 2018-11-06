# check if the word secret exists in a string and if not return false
stringi = 'a trylly secret string'


def printer(string):
    for index in string:
        if index in 'secret':
            return True
        else:
            return False


# create a function that change the letter b in a string if exists to something of your choice
def letter_changer(someString):
    output = list(someString)
    for index, letter in enumerate(someString):
        if letter == 'b':
            output[index] = 'e'
    output = ''.join(output)
    return output


print(letter_changer('bla bla bla'))

# create a function that takes 2 numbers and returns true if the sum is equal and more to 10


def numbers(num1, num2):
    sum = num1 + num2
    if sum >= 10:
        return True
    else:
        return False


print(numbers(5, 5))


def numbers2(num1, num2):
    sum = num1 + num2
    if sum == 10:
        return True
    else:
        return sum


print(numbers2(10, 6))

# create a function that takes a string and returns back the first character of that string in upper case


def stringCapital(string):
    return string[0].upper()


print(stringCapital('something'))


# create a function that takes a string and returns the last 2 characters
# if there is less than 2 characters return the string 'error'


def stringCut(string):
    if len(string) < 2:
        return 'error'
    else:
        return string[-2:]


print(stringCut('randomstring'))
