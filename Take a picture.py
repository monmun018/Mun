#問題
#https://www.codewars.com/kata/56c9f47b0844d85f81000fc2
import re
def extract_number(string):
	res = re.findall(r'\d+', string)
	return list(map(int,res))
def sort_photos(pics):
    print(pics)
    pics = sorted(pics, key = extract_number)
    k = pics[-1].find('g') +1
    pics.append(pics[-1][:k:]+str(int(pics[-1][k::])+1))
    return pics[len(pics)-6::1] if len(pics) >=5 else pics
