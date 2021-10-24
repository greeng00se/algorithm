import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
result = 0

for i in range(n - 1):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    
def dfs(x):
    global result
    if not adj[x]:
        return 0

    diameter = []
    maxValue = 0
    for node in adj[x]:
        nxt, v = node
        tmp = v + dfs(nxt)
        diameter.append(tmp)
        maxValue = max(maxValue, tmp)
    diameter.sort(reverse = True)
    result = max(result, sum(diameter[:2]))
        
    return maxValue
    
dfs(1)
print(result)