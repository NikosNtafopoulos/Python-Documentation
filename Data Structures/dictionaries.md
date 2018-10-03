# What is a dictionary?

### A data structure which is unordered and has a set of `key:value` pair

### According to official python documentation we can found dictionaries on other languages refered as `associative memories` , `associative arrays`[unlike sequence which are indexed by a range of numbers] or as `hashmaps`,dictionaries are indexed by keys[a unique identifier] and values[data]

### if we try to access a key tha doesn't exist in our dictionary python's interpreter will throw a keyError:

```
KeyError: 'keythatdoesntexist'
```

### A very usefull method whould be with get() and parse our default message if a key doesn't exists

```
print clientInfo.get('orderss','key not found')
```

### if you try to pass a key tha exists with an extra arg like this:

```
print clientInfo.get('orders', 'changetestestestest')

# output
['laptop', 'tablet', 'smartphone']
```
