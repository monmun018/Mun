# 問題
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
import math
def is_square(n):    
    return False if n<0 else int(math.sqrt(n))**2==n