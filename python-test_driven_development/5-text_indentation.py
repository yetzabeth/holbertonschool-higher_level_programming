#!/usr/bin/python3
''' Write a function that prints a text with 2 new lines after each of thes'''


def text_indentation(text):
    ''' text  identation  '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    x = text.replace('?', '?\n\n').replace(':', ':\n\n').replace('.', '.\n\n')
    new_text = x.replace('\n ', '\n')
    if new_text[:-1] == '\n':
        del new_text[:-1]
    print(new_text, end='')
