#問題
#https://www.codewars.com/kata/541c8630095125aba6000c00
def add(m):
    return sum(int(x) for x in str(m))

def digital_root(n):
    while len(str(n))>1:
        n = add(n)
    return(n)
