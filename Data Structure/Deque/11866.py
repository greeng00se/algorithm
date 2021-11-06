from collections import deque

n, m = map(int, input().split())
dq = deque()
for i in range(n):
    dq.append(i + 1)
    
result = []
while dq:
    dq.rotate(-m + 1)
    result.append(dq.popleft())
    
print('<', end = '')
print(*result, sep = ', ', end = '')
print('>')
    