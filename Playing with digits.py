#問題
# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    result = 0
    temp = n
    temp = list(str(n))
    for x in range(len(temp)):
        result+= int(temp[x])**p
        p+=1   
    return result//n if result%n == 0 else -1
