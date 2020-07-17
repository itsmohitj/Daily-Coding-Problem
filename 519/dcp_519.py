def solution(x,y,b):
    b=-b
    return((x and b) or (y and (~b)))
