#問題
#https://www.codewars.com/kata/5eb27d81077a7400171c6820
from math import ceil 
def graceful_tipping(bill):
    bill = ceil(bill*1.15)
    if bill < 10 :
        return bill
    else:
        divi = 5*10**(len(str(bill))-2)
        return ceil(bill/divi)*divi