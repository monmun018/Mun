#問題
# https://www.codewars.com/kata/58845748bd5733f1b300001f
def range_bit_count(a, b):
    return ''.join(map(lambda m:str(bin(m)),range(a,b+1))).count('1')
