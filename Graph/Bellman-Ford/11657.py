import sys

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))

def bellman_ford():
    distance = [INF] * (n + 1)
    distance[1] = 0
    
    for _ in range(n - 1):
        for i in range(1, n + 1):
            for node in adj[i]:
                nxt, w = node
                if distance[i] != INF and distance[nxt] > distance[i] + w:
                    distance[nxt] = distance[i] + w
    
    for i in range(1, n + 1):
        for node in adj[i]:
            nxt, w = node
            if distance[i] != INF and distance[nxt] > distance[i] + w:
                print(-1)
                return
    
    for i in range(2, n + 1):
        if distance[i] >= INF: print(-1)
        else: print(distance[i])
        
bellman_ford()
        
        