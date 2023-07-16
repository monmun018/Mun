#問題
#https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    re_list = [ str(int(i)**2) for i in str(num)]
    return int(''.join(re_list))
