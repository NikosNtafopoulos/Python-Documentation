# What is a list?

### A data structure sequence which is ordered and mutable

# What is a tuple?

### A data structure sequence which is ordered and immutable

### they are exactly like lists except they start with `(` instead of `[` and their values cannot be changed which means that we can not append or remove elements

# What is a set?

### A data structure collection which is unordered and immutable.Also a set value is unique which means that does not have dublicate members

# Sets values are unorder and have not duplicates

### starts with `{`

# How to access the elements of my list?

### exampleElement[0] --> will grab the first item in our list,[1] our second item [2] our third and goes on ......Lists are very similar with arrays in other programming languages[we always count from 0]

### exampleElement[-1] --> will grab the LAST item in our list

# If we have a list with 5 elements how can i access the first 3 elements?

```
 exampleElements = ['test','test2','test2','test3','test4']


 exampleElements[0:3]
```

# And if we want the other 2 elements of our list?

```
 exampleElements[3:]
```

# How to add an item in my list?

## with append

```
 exampleElements.append('test5')
```

# If we want the item to be in the start??

```
 exampleElements.insert(0, 'test5')
```

# If we want to remove something from our list?

### With the remove() method which takes a sigle element as an argument and removes it from the list.If the item does not exist it will display a valueError exception

# How to check if an item exists in my list?

```
UniCourses = ['history','Maths','Art']

for item in UniCourses:
    print item

for history in UniCourses:
    print history
```

# And how about if we want to print the index?

```
 for index, course in enumerate(UniCourses):
     print(index, UniCourses)
```

---

###### Check the `examples`.py for further sequence,collection examples
