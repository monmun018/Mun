#問題
#https://www.codewars.com/kata/525c65e51bf619685c000059
def cakes(recipe, available):
    checking = len( [i for i in list(recipe.keys()) if i not in list(available.keys()) ])
    return min(list(map(lambda k:available[k]//recipe[k],list(recipe.keys())))) if not checking else 0
