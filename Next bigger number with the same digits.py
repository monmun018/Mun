#問題
#https://www.codewars.com/kata/55983863da40caa2c900004e
def next_bigger(n):
    result = -1
    sd = list(map(int , [x for x in str(n)]))
    for i in range(len(sd)-1):
        if sd[-i-1] > sd[-i-2]:
            key = min([x for x in sd[-i-1:] if x > sd[-i-2]])
            new_list = sd[-i-2:]
            new_list.remove(key)
            new_list.sort()
            return int("".join(map(str,sd[:-i-2]))+str(key)+"".join(map(str,new_list)))
    return -1