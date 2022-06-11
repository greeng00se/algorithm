import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
power = []
result = 0

for i in range(k):
    if data[i] in power:
        continue
    
    if n > len(power):
        power.append(data[i])
        continue
    
    result += 1
    
    if n == 1:
        power[0] = data[i]
        continue
        
    idxs = []
    for p in range(n):
        try: idxs.append((data[i+1:].index(power[p]), p))
        except: idxs.append((101, p))
        
    idxs.sort(reverse = True)
    del power[idxs[0][1]]
    power.append(data[i])
    
print(result)

