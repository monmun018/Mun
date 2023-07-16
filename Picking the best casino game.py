#問題
#https://www.codewars.com/kata/5dfd129673aa2c002591f65d
def find_best_game(games):
    result = list()
    for i in games:
        result.append([i.name, sum(a*b for a,b in i.outcomes)]) 
    return max(result, key = lambda a: a[1])[0]