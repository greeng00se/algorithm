import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
a = {}

for i in range(n):
    for j in range(n):
        x = data[i][0] + data[j][1]
        if x in a: a[x] += 1
        else: a[x] = 1
        
result = 0
for i in range(n):
    for j in range(n):
        if -(data[i][2] + data[j][3]) in a:
            result += a[-(data[i][2] + data[j][3])]
print(result)
        