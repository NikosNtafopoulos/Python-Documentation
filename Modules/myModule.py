# variables
print 'hello from myModule'
testMe = 'Just Test me '
myUsename = 'Nikos'
myPassword = str(23)+'a'+str(56)+'#'
loop = True
importedVar = "I'am imported"


# functions


def index(lista, target):
    for l, t in enumerate(lista):
        if t == target:
            return l
    return '{} item not found'.format(target)


def login(username, password):
    while(loop == True):
        if(username == myUsename and password == myPassword):
            #loop == False
            return 'You are logged in'
        else:
            return 'Try a different combination'


def randomFunction(a, b):
    if a == b:
        return True
    else:
        return False


def checkIfString(item):
    if item == str(item):
        return True
    else:
        return "Number"
