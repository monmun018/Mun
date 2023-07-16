#問題
#https://www.codewars.com/kata/52f3149496de55aded000410
def sum_digits(number):
    number = str(number)
    return  sum( list( map(lambda a: abs(int(a)),[j for j in list(number) if j.isdigit()]) ))
