#問題
# https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef
def find_children(santas_list, children):
    return sorted(x for x in santas_list if x in children)
