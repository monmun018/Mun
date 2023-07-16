#問題
#https://www.codewars.com/kata/5a908da30025e995880000e3
from math import sqrt
def prime_num(n):
    for i in range(2,int(sqrt(n)+1)):
        if not n % i:
            return False
            break
    else: 
        return True

def solve(a, b):
    prime = "2"
    n = 3
    while a+b> len(prime):
        if prime_num(n):
            prime = prime + str(n)
        n+=2
    return prime[a:a+b]