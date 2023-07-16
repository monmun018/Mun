#問題
#https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    return ' '.join(list(map(lambda a: a[-1::-1] if len(a) >= 5 else a ,sentence.split(' ')))) 
