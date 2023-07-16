#問題
#https://www.codewars.com/kata/550498447451fbbd7600041c
def comp(array1, array2):
    return not None in (array1,array2) and sorted([i*i for i in array1]) == sorted(array2)