#問題
#https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    sorted_list = []
    var_list =  sentence.split()
    for i in range(1,10):
        sorted_list.extend([j for j in var_list if str(i) in list(j)])
    return " ".join(sorted_list)
