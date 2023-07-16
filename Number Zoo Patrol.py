#問題
#https://www.codewars.com/kata/5276c18121e20900c0000235
def find_missing_number(numbers):
    n = len(numbers)+1
    return n*(n+1)//2-sum(numbers)