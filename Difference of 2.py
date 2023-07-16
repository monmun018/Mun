#問題
#https://www.codewars.com/kata/5340298112fa30e786000688
def twos_difference(lst): 
    a = sorted(lst)
    result = [ x for x in a if x+2 in a]
    result = [(x,x+2) for x in result]
    return result