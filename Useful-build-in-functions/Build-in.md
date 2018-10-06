Python has very useful build-in functions to interact
Let's see some of them

```
word = 'Welcome'
#return the length of an object
len(Welcome)
```

also len can accept a sequence(such a string,bytes,tuples,list,range) or a collection such as a dictionary or set

python strings methods

- .upper() --> convers a string into upper case
- .join() --> joins the elements of an iterable to the end of the string
- .replace() --> returns a string where a specified value is replaced with a specified value
- .lower() --> Converts a string into lower case

python list methods

- .append() --> adds an element at the end of the list
- .remove() --> removes the first item with the specified value
- .count() --> returns a number of the elements with the specified value
- .copy() --> returns a copy list
- .clear() --> removes all the elements from the list

python dictionary methods

- .values() --> returns a list of all the values in dictionary
- .clear() --> revomes all the elements from the dictionary
- .copy() --> returns a copy of the dictinary
- .pop() --> removes the element with the specified key
- .popitem() --> removes the last inserted key-value pair
- .updates() --> updates the dictionary with the specified key-value pairs

Most of pythons methods are only for a given value type such as `.upper()` wich works with strings,but not for integers.And .append() works with lists only and doesn't work with strings,integers or booleans
