#問題
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
def descending_order(num):
    return int(''.join(x for x in sorted(str(num),reverse=True)))
