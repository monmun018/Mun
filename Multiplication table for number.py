#問題
#https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
def multi_table(number):
    re_list = ['{} * {} = {}'.format(i,number,i*number) for i in range(1,11)]
    return "\n".join(re_list)