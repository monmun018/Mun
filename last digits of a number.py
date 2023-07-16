#問題
#https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0
def solution(n,d):
    print(n,d);
    return list(map(int, list(str(n))[-d:])) if d > 0 else []