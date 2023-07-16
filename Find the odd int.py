#問題
#https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    temp = list(set(seq))
    for x in temp:
        if seq.count(x) % 2 == 1:
            result = x
            break
    return result