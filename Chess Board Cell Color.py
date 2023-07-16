#問題
#https://www.codewars.com/kata/5894134c8afa3618c9000146
def chess_board_cell_color(cell1, cell2):
    return True if (ord(cell1[0])-ord(cell2[0]) + int(cell1[1]) - int(cell2[1])) % 2 == 0 else False