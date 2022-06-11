import sys

input = sys.stdin.readline

p = [list(map(int, input().split())) for _ in range(3)]

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    
result = ccw(p[0], p[1], p[2])
print(1 if result > 0 else 0 if result == 0 else -1)