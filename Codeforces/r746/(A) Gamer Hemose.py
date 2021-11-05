import sys

input = sys.stdin.readline

rep = int(input())
for _ in range(rep):
    a, b = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort(reverse = True)
    c, d = data[0], data[1]
    
    if b <= c:
        print(1)
        continue
    
    result = (b // (c + d)) * 2
    p = (c + d) * (result // 2)
    if p >= b:
        print(result)
    elif p + c >= b:
        print(result + 1)
    else:
        print(result + 2)
            
    