import sys

input = sys.stdin.readline

er = [0] * 250000
er[0], er[1] = 1, 1

for i in range(2, 250000):
    if er[i]: continue
    for j in range(i * i, 250000):
        if j % i == 0: 
            er[j] = 1

while True:
    n = int(input())
    if n == 0: break
    
    result = 0
    for i in range(n + 1, n * 2 + 1):
        if not er[i]: result += 1
            
    print(result)

