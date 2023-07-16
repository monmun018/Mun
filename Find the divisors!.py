#問題
#https://www.codewars.com/kata/544aed4c4a30184e960010f4
def divisors(integer):
    result = [x for x in range (2,integer) if integer % x == 0]
    if result == []:
        return "{} is prime".format(integer)
    else:
        return result