# What is a function???

### A function is a set of instructions packaged together that performs a specific task

# How to write a function in python

### With the special keyword `def` the name of the function, followed by parenthensis(with args or not) and `:`

```
def calculations ():
    pass
```

### What is `pass` ?

#### It's used when a statement is required but we don't want any commands or code block to be executed

- pass statement is a null operation

# What is the meaning of args and kwargs?

### args --> in case of we don't know how many arguments the user is going to pass, args is used to send a non-keyworded variable length argument list to the function

### kwargs --> allows you to pass keyworded variable lengths of arguments to a function

### Let's see a function for the total revenue [Functions/test.py]

#### if we pass \*args as argument we don't have to give arguments to our function everytime we call it

```
#output
Enter your price: 4
Enter a desirable quantity: 5
Total Revenue is: 20€
```
