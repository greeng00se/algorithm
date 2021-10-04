import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
lines = []
r = [0] * 500001
for _ in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])
    r[b] = a
    
    
lines.sort()

q = []
temp = []
for line in lines:
    line = line[1]
    if not q or line > q[-1]:
        q.append(line)
        temp.append((len(q) - 1, line))
    else:
        q[bisect_left(q, line)] = line
        temp.append((bisect_left(q, line), line))
        
goodline = []
result = []
last_idx = len(q) - 1
for i in range(len(temp) - 1, -1, -1):
    if temp[i][0] == last_idx:
        goodline.append(temp[i][1])
        last_idx -= 1
    else:
        result.append(temp[i][1])

answer = []
print(len(result))
for i in result:
    answer.append(r[i])
answer.sort()
for i in answer:
    print(i)