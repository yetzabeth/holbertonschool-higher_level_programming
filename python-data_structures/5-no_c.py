#!/usr/bin/python3
def no_c(my_string):
    new = my_string.translate({ord(i): None for i in 'Cc'})
    return new
