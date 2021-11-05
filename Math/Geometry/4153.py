import sys
import math

input = sys.stdin.readline

def isTriangle(points):
    a, b, c = points
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False
    
while True:
    points = list(map(int, input().split()))
    if points[0] == 0: break
    points.sort()
    if isTriangle(points):
        print('right')
    else:
        print('wrong')
    