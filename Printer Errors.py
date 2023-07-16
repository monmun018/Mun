#問題
# https://www.codewars.com/kata/56541980fa08ab47a0000040

def printer_error(s):
   t = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   temp = sum(map(lambda a:s.count(a),t))
   return str(temp)+'/'+str(len(s))
