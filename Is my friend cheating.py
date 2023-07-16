#問題
# https://www.codewars.com/kata/5547cc7dcad755e480000004
def removNb(n):
    result = []
    n_list = list(range(1,n+1))
    n_sum = sum(n_list)
    for x in n_list:
        if (n_sum-x)%(x+1) == 0  and (n_sum-x)/(x+1) in n_list:
            result.extend([(x,int((n_sum-x)/(x+1)))])
    return result