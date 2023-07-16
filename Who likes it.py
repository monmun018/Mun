#問題
#https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    if not names:
        result = "no one likes this"
    elif len(names) == 1:
        result = "{} likes this".format(names[0])
    elif len(names) == 2:
        result = "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3:
        result = '{}, {} and {} like this'.format(names[0], names[1], names[2])
    elif len(names) >= 4:
        result = "{}, {} and {} others like this".format(names[0], names[1],len(names)-2)
    return result