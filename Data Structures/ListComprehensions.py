nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i want 'n' for each 'n' in nums
myList = []
for n in nums:
    myList.append(n)
print myList
# or
myNewList = [n for n in nums]
print myNewList

for n in nums:
    print n.numerator

# n*n for each 'n' in nums
myList2 = []
for n in nums:
    myList2.append(n*n)
print myList2

# list comprehension
my_list = [n*n for n in nums]
print my_list

# using a map+lambda(anonymous function)
my_list2 = map(lambda n: n*n, nums)
print my_list2


# 'n' for each 'n' in nums if 'n' is even
myList = []
for n in nums:
    if n % 2 == 0:
        myList.append(n)
    print myList
# list comprehension
myListC = [n for n in nums if n % 2 == 0]
print myListC
# lambda
myListLmbd = filter(lambda n: n % 2 == 0, nums)
print myListLmbd

# i want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print my_list
# list comprehension
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print my_list
