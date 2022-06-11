import sys 
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
INF = int(1e9)
distance = [INF] * 100001

def dijkstra(s):
    hq = []
    visited = [0] * (100001)
    distance[s] = 0
    heapq.heappush(hq, (0, s))
    
    while hq:
        dist, now = heapq.heappop(hq)
        if visited[now]:
            continue
            
        visited[now] = 1
            
        if now + 1 <= 100000 and not visited[now + 1] and distance[now + 1] > dist + 1:
            distance[now + 1] = dist + 1
            heapq.heappush(hq, (distance[now + 1], now + 1))
        if now - 1 >= 0 and not visited[now - 1] and distance[now - 1] > dist + 1:
            distance[now - 1] = dist + 1
            heapq.heappush(hq, (distance[now - 1], now - 1))
        if now * 2 <= 100000 and not visited[now * 2] and distance[now * 2] > dist:
            distance[now * 2] = dist
            heapq.heappush(hq, (distance[now * 2], now * 2))
            
    print(distance[k])
                
dijkstra(n)