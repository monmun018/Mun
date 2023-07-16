#問題
#https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
def clean_string(s):
    result =[]
    for i in s:
        if i != '#':
            result.append(i)
        elif len (result):
            result.pop()
    return ''.join(result)