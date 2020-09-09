"""
This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""


def solution(x,y,b):
    b=-b
    return((x and b) or (y and (~b)))
