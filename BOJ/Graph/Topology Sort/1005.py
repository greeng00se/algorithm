import sys
import heapq

input = sys.stdin.readline

rep = int(input())
INF = int(1e9)

def ts():
    result = [0] * (n + 1)
    hq = []
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(hq, (d[i - 1], i))
    
    while hq:
        time, now = heapq.heappop(hq)
        result = time
        if now == w:
            break
        
        for node in adj[now]:
            indegree[node] -= 1
            
            if indegree[node] == 0:
                heapq.heappush(hq, (d[node - 1] + time, node))
                
    print(result)
                
for _ in range(rep):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        adj[a].append(b)
        indegree[b] += 1
        
    w = int(input())
    ts()