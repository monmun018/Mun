#問題
# https://www.codewars.com/kata/54ff3102c1bad923760001f3
def getCount(inputStr):
    return sum(list(map(lambda k:inputStr.count(k),list('aiueo'))))
