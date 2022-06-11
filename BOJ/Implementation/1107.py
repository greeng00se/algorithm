from itertools import product

a = int(input())
b = int(input())
c = []
if b: c = list(map(str, input().split()))
num = set([str(i) for i in range(10)])
num = num - set(c)
now = 100

result = int(1e9)

for i in range(7):
    if not num: break
    for j in list(product(list(num), repeat=i)):
        if not j: continue
        n = int(''.join(j))
        n = abs(a - int(''.join(j)))
        if n + i < result:
            result = n + i
            
if abs(now - a) < result:
    result = abs(now - a)
            
print(result)
