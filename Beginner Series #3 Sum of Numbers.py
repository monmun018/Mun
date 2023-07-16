#問題
#https://www.codewars.com/kata/55f2b110f61eb01779000053
def get_sum(a,b):
    return a if a == b else sum(range(a,b+1)) if a<b else sum(range(b,a+1))
