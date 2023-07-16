#問題
#https://www.codewars.com/kata/52549d3e19453df56f0000fe
#回答１
def fib(n):
    a1,a2=0,1
    for i in range(n-1):
        a1,a2 = a2, a1+a2
    return a1
# 回答２
def fib(n):
    a1,a2=0,1
    if n==1:
        return a1
    elif n==2:
        return a2
    else:
        for i in range(n-2):
            a1,a2= a2,a1+a2
        return a2  