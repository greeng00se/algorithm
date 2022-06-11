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
    
    if ab == cd == 0:
        if a > b: a, b = b, a
        if c > d: c, d = d, c
        return c <= b and a <= d
    return ab <= 0 and cd <= 0;
    
if isIntersect(point[0], point[1], point[2], point[3]):
    a, b, c, d = point
    print(1)
    try:
        px = (a[0] * b[1] - a[1] * b[0]) * (c[0] - d[0]) - (a[0] - b[0]) * (c[0] * d[1] - c[1] * d[0])
        py = (a[0] * b[1] - a[1] * b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] * d[1] - c[1] * d[0])
        p = (a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0])
        print(px / p, py / p)
    except:
        if a > b: a, b = b, a
        if c > d: c, d = d, c
        if b == c: print(*b)
        elif a == d: print(*a)
else: print(0)
