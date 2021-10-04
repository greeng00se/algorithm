import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

rep = int(input())

def dfs(x):
    global result
    visited[x] = 1
    t.append(x)
    
    nt = data[x]
    if visited[nt]:
        if nt in t:
            result += len(t[t.index(nt):])
        return
    else:
        dfs(nt)
    
for _ in range(rep):
    n = int(input())
    result = 0
    data = list(map(int, input().split()))
    data.insert(0, 0)
    visited = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            t = []
            dfs(i)
            
    print(n - result)
    
    
    
