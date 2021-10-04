import sys

input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
result = 0
parent = [i for i in range(v + 1)]
s = [1] * (v + 1)
c = v - 2

for _ in range(e):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))
    
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
    c -= 1
    if not c:
        break
    
print(result)


