#問題
#https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers):
    return [ x for x in integers if (x + integers[integers.index(x)-1])%2==1 and (x + integers[integers.index(x)-2])%2==1][0]