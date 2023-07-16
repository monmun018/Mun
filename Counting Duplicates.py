#問題
#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1 

def duplicate_count(text):
    text = text.lower()
    return len([x for x in set(text) if text.count(x)>1])
