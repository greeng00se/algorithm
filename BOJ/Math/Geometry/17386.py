import sys

input = sys.stdin.readline

point = []
for i in range(2):
    a, b, c, d = map(int, input().split())
    point.append((a, b))
    point.append((c, d))

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    return 1 if result > 0 else -1 if result < 0 else 0

def isIntersect(a, b, c, d):
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    return ab <= 0 and cd <= 0;
    
print(int(isIntersect(point[0], point[1], point[2], point[3])))