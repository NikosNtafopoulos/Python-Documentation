'''Lists'''

UniCourses = ['distributed Systems', 'mathematics', 'design patterns']
AllCourses = ['Economics', 'Art', 'Games']
# append the AllCourses on UniCourses list
UniCourses.extend(AllCourses)
print UniCourses
print AllCourses.index('Games')
''' if we don't want the 0 index we can add after UniCourses,start = 1 (UniCourses, start = 1) as args '''
for index, item in enumerate(UniCourses):
    print index, item
UniCoursesStr = '-'.join(UniCourses)
print UniCoursesStr

# Sorting
UniCourses.reverse()
print(UniCourses)

UniCourses.sort()
print(UniCourses)
# Instead of this we can do like this
UniCourses.sort(reverse=True)
# Or
sortedCourses = sorted(UniCourses)
print sortedCourses
# With numbers
numbers = [2, 10, 6, 1, 3, 9]
numbers.sort()
print numbers

# sum min max
print sum(numbers)
print min(numbers)
print max(numbers)

UniCourses2 = ['history', 'Maths', 'Art']
# for item in UniCourses:
#   print itm

for history in UniCourses2:
    print history

math = ['math']

# function for a simple check up with string output

# put math instead of history and see the output


def checker(list):
    if history in list:
        return '{} item  exists in {}'.format(history, list)
    else:
        return 'No Item with the name {} in {}'.format(math, list)


checker(UniCourses2)
print checker(UniCourses2)
print UniCourses2[0:1]
