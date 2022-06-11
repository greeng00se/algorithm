import sys

input = sys.stdin.readline

INF = int(1e9)
rep = int(input())

def bellman_ford(n, adj):
    distance = [INF] * (n + 1)
    distance[1] = 0
    for _ in range(n - 1):
        for i in range(1, n + 1):
            for node in adj[i]:
                nxt, w = node
                if distance[nxt] > distance[i] + w:
                    distance[nxt] = distance[i] + w

    for i in range(1, n + 1):
        for node in adj[i]:
            nxt, w = node
            if distance[nxt] > distance[i] + w:
                return 'YES'
    return 'NO' 
    
for _ in range(rep):
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))
        adj[b].append((a, w))
    
    for i in range(k):
        a, b, w = map(int, input().split())
        adj[a].append((b, -w))
    print(bellman_ford(n, adj))
