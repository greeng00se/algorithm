import sys
import math

input = sys.stdin.readline

v = int(input())
planet = []
result = 0
parent = [i for i in range(v + 1)]
s = [1] * (v + 1)

for i in range(v):
    a, b, c = map(int, input().split())
    planet.append((a, b, c, i))

edges = []
for i in range(3):
    planet.sort(key = lambda x : x[i])
    for j in range(v - 1):
        a1, b1, c1, d1 = planet[j]
        a2, b2, c2, d2 = planet[j + 1]
        edges.append((min(abs(a1 - a2), abs(b1 - b2), abs(c1 - c2)), d1, d2))
        
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


