#!/usr/bin/python3
"""print line after specified chars"""


def text_indentation(text):
    """
     print a text with 2 new lines after each of these characters: ., ? and :
     Args:
        param1 (text): the text to be searched
    Exception:
        TypeError: if the provided text is not string
    """
    ans = ""
    space = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            space += 1
            ans += i
            ans += '\n\n'
        else:
            if space == 1 and i == ' ':
                True
            else:
                ans += i
            space = 0
    print(ans, end='')
