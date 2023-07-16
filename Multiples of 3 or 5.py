#問題
#https://www.codewars.com/kata/514b92a657cdc65150000006
def solution(number):
    temp = []
    for x in range(number):
        if x%3 ==0 or x %5==0:
            temp.append(x)
    return sum(temp)
