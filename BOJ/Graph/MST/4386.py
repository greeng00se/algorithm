import sys
import math

input = sys.stdin.readline

v = int(input())
stars = []
result = 0
parent = [i for i in range(v + 1)]
s = [1] * (v + 1)

for _ in range(v):
    a, b = map(float, input().split())
    stars.append((a, b))
    
edges = []
for i in range(v):
    a1, b1 = stars[i]
    for j in range(i + 1, v):
        a2, b2 = stars[j]
        edges.append((math.sqrt(abs(a1 - a2) ** 2 + abs(b1 - b2) ** 2), i, j))
        
edges.sort()

def union(x, y):
    a = find(x)
    b = find(y)
    if s[a] > s[b]:
        a, b = b, a
    parent[a] = b
    s[b] += s[a]
    
def find(x):
    if parent[x] == x: return x
    else: 
        parent[x] = find(parent[x])
        return parent[x]
    
for edge in edges:
    w, a, b = edge
    if find(a) == find(b):
        continue
    union(a, b)
    result += w
    
print(result)


