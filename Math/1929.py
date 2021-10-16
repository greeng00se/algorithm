import sys

input = sys.stdin.readline

n, m = map(int, input().split())
eratos = [0] * (m + 1)
eratos[0], eratos[1] = 1, 1

for i in range(2, (m + 1)):
    if eratos[i]:
        continue
    for j in range(i * i, (m + 1)):
        if j % i == 0:
            eratos[j] = 1
        
for i in range(n, (m + 1)):
    if not eratos[i]:
        print(i)
        