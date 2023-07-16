#問題
#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    new_list = list(s)
    result =[]
    for x in range(len(s)):
        result.append((new_list[x]*(x+1)).capitalize())
    return "-".join(result)
