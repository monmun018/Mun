#問題
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def mul(num):
    result = 1
    for i in list(str(num)):
        result*= int(i)
    return result
def persistence(n):
    result = 0
    while len(str(n))>1:
        n = mul(n)
        result +=1
    return result
