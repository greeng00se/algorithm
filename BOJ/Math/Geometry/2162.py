import sys

input = sys.stdin.readline

n = int(input())
lines = [[] for _ in range(n + 1)]
for i in range(n):
    a, b, c, d = map(int, input().split())
    lines[i] = [(a, b), (c, d)]

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
    

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [i for i in range(n)]
parentCount = [0] * n
groupCount = 0
result = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if isIntersect(lines[i][0], lines[i][1], lines[j][0], lines[j][1]):
            union_parent(parent, i, j)
            
for i in range(n):
    if parent[i] == i:
        groupCount += 1
    now = find_parent(parent, i)
    parentCount[now] += 1
    if parentCount[now] > result:
        result = parentCount[now]

print(groupCount, result, sep = '\n')