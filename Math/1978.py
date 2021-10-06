import sys

input = sys.stdin.readline

MAX = 1001

n = int(input())
data = list(map(int, input().split()))
result = 0
eratos = [0] * MAX
eratos[0], eratos[1] = 1, 1

for i in range(2, MAX):
    if eratos[i]: 
        continue
    for j in range(i * i, MAX):
        if j % i == 0: 
            eratos[j] = 1
            
for i in data:
    if not eratos[i]:
        result += 1
        
print(result)
    