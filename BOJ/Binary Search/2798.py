import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            result.append(data[i] + data[j] + data[k])
            
result.sort(reverse = True)
for i in result:
    if i > m: continue
    print(i)
    break
            