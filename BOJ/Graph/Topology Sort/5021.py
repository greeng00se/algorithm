import sys
from collections import deque

n, m = map(int, input().split())
king = input()
royal = {}

# adj, ratio, indegree, parent
royal[king] = [[], 100, 0, []]

for _ in range(n):
    people = list(map(str, input().split()))
    for i in people:
        if i not in royal.keys(): royal[i] = [[], 0, 0, []]
    
    a, b, c = people
    royal[b][0].append(a)
    royal[c][0].append(a)
    royal[a][2] += 2
    royal[a][3] = [b, c]
    
def topology():
    queue = deque()
    
    for i in royal:
        if royal[i][2] == 0:
            queue.append(i)
            
    while queue:
        now = queue.popleft()
        if royal[now][3]:
            a, b = royal[now][3]
            royal[now][1] = (royal[a][1] + royal[b][1]) / 2
        for node in royal[now][0]:
            royal[node][2] -= 1
            if royal[node][2] == 0:
                queue.append(node)
                
    result = ''
    top = 0
    for i in range(m):
        who = input()
        if who in royal.keys() and royal[who][1] > top:
            result = who
            top = royal[who][1]
            
    print(result)
                
topology()