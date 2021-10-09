import sys

input = sys.stdin.readline

rep = int(input())

po = []
for i in range(31):
    po.append((2 ** i, i))
po.reverse()

result = []

for _ in range(rep):
    a, b = map(int, input().split())
    result = []
    for i in po:
        if b < i[0]: continue
        b -= i[0]
        result.append(a ** i[1])
        
    print(sum(result) % (int(1e9) + 7))
    