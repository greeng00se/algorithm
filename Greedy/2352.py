import sys

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
k = int(input())
if k > n: k = n
data = sorted(list(map(int, input().split())))
dif = []
cut = []
result = 0

for i in range(n - 1):
    a, b = data[i], data[i + 1]
    dif.append((abs(a - b), i, i + 1))
    
dif.sort()

for i in range(k - 1):
    cut.append(dif.pop())

cut.sort(key = lambda x : x[1])

j = 0
l, r = INF, INF
for i in range(n):
    if l == INF: l = data[i]
    r = data[i]
    if (j < k - 1 and cut[j][1] == i) or i == n - 1:
        result += r - l
        l = r = INF
        j += 1
    
print(result)
        
    
    