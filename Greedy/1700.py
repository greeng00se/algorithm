import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
tap = [0] * n
result = 0

for i in range(k):
    if data[i] in tap:
        continue
    
    if 0 in tap: 
        tap[tap.index(0)] = data[i]
        continue
    
    flag = 0
    count = set()
    for m in range(i + 1, k):
        if n == 1 or flag: break
        for j in tap:
            if j == data[m]:
                count.add(j)
                break
        if len(count) == n - 1:
            q = set(tap) - count
            tap[tap.index(list(q)[0])] = data[i]
            flag = 1
            result += 1
            break
    if flag: continue
    q = set(tap) - count
    tap[tap.index(list(q)[0])] = data[i]
    result += 1
    
print(result)

