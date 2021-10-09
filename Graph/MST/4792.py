import sys

input = sys.stdin.readline

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
    
def st(edges, flag):
    result = [0, 0]
    
    for i in range(2):
        for edge in edges[i ^ flag]:
            a, b = edge
            if find(a) == find(b):
                continue
            union(a, b)
            result[i ^ flag] += 1
    return result[0]

while True:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break
    edges = [[], []]
    parent = [i for i in range(n + 1)]
    s = [1] * (n + 1)
    for _ in range(m):
        c, a, b = map(str, input().split())
        a, b = int(a), int(b)
        if c == 'B': edges[0].append((a, b))
        else: edges[1].append((a, b))
    
    a = st(edges, 0)
    parent = [i for i in range(n + 1)]
    s = [1] * (n + 1)
    b = st(edges, 1)
    if b <= k <= a: print(1)
    else: print(0)
    
    


