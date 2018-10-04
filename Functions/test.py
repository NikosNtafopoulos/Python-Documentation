#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Those 2 line of comment code are for the euro symbol
if you remove tha block it will throw a SyntaxError: Non-ASCII character'''


''' lets see a simple economic formula
    Total Revenue(AR) = Price X Quantity   '''

# function for a user to interact

# i'm using *args just for testing dynamic input  and is working


def totalRev(*args):
    price = int(input('Enter your price: '))
    quantity = int(input('Enter a desirable quantity: '))
    Tr = price * quantity
    return 'Total Revenue is: ' + str(Tr) + '€'


print totalRev()
