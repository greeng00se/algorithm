import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
l, r = [], []
result = 1e9
    
def dfs(x):
    global result
    if x == n:
        lsum, rsum = 0, 0
        for i in l:
            for j in l:
                if i == j: continue
                lsum += a[i][j]
        for i in r:
            for j in r:
                if i == j: continue
                rsum += a[i][j]
        
        if abs(lsum - rsum) < result:
            result = abs(lsum - rsum)
        return
    
    if len(l) < n // 2:
        l.append(x)
        dfs(x + 1)
        l.pop()
    if len(r) < n // 2:
        r.append(x)
        dfs(x + 1)
        r.pop()
        
dfs(0)
print(result)