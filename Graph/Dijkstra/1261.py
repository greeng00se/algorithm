import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(m)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x >= m or y >= n or x < 0 or y < 0

def dijkstra():
    visited = [[INF] * n for _ in range(m)]
    hq = []
    heapq.heappush(hq, (0, 0))
    visited[0][0] = 0
    
    while hq:
        r, c = heapq.heappop(hq)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if isout(nr, nc): 
                continue
            
            v = 1 if data[nr][nc] else 0
            if visited[nr][nc] > visited[r][c] + v:
                heapq.heappush(hq, (nr, nc))
                visited[nr][nc] = visited[r][c] + v
    
    print(visited[m - 1][n - 1])
    
dijkstra()
                
        
    