#問題
#https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a, b):
    for x in b:
        while x in a:
            a.remove(x)
    return a