#問題
#https://www.codewars.com/kata/5868812b15f0057e05000001
def tail_swap(strings):
    str1 , str2 = strings
    i1 = len(str1) - str1.find(":") -1
    i2 = len(str2) - str2.find(":") -1
    return [str1[:-i1]+str2[-i2:],str2[:-i2]+str1[-i1:]]