#問題
#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
def solution(s):
    if len(s) % 2 == 1:
        s = s + "_"
    s = list(s)
    result = []
    for x in [a for a in range(len(s)) if a % 2 == 0]:
        result.append(s[x]+s[x+1])
    return result