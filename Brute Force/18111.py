import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
data = [0] * 257
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in tmp: data[j] += 1
        
time = []

for i in range(257):
    result = 0
    block = v
    for j in range(257):
        if data[j] == 0: continue
        if j > i:
            block += (j - i) * data[j]
            result += (j - i) * 2 * data[j]
        if j < i:
            block -= (i - j) * data[j]
            result += (i - j) * data[j]

    if block < 0: continue
    time.append((result, i))
    
time.sort(key = lambda x: (x[0], -x[1]))
print(*time[0])
