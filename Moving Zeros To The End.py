#問題
#https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(array):
    #Fix 0.0
    for x in range(len(array)):
        if str(array[x]) == '0.0':
            array[x] = 0
    ###
    result = [x for x in array if x is not 0]
    m = [0]*(len(array)-len(result))
    result.extend(m)
    return result