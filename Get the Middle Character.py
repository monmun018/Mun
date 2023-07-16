#問題
#https://www.codewars.com/kata/56747fd5cb988479af000028
def get_middle(s):
    k = len(s)
    if k%2==0:
        result = s[k//2-1:k//2+1]
        print(k//2)
    else: 
        result = s[(k//2)] 
    return result