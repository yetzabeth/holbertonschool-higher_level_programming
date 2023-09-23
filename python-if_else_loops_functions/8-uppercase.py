#!/usr/bin/python3
def islower(c):
    i = ord(c)
    if i > 96 and i < 123:
        return True
    else:
        return False


def uppercase(str):
    upper = ''
    for i in str:
        if islower(i):
            i = chr(ord(i) - 32)
        print('{}'.format(i), end='')
    print('')
