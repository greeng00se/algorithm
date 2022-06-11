import sys

input = sys.stdin.readline

while True:
    n, a, b = map(int, input().split())
    result = 0
    p = []
    if n == a == b == 0: break
    
    for i in range(n):
        num, da, db = map(int, input().split())
        p.append((abs(da - db), num, da, db))
    
    p.sort(reverse = True)

    for i in range(n):
        _, num, da, db = p[i]
        if da > db:
            mv = min(b, num)
            result += db * mv
            b -= mv

            num -= mv
            result += da * num
            a -= num
        else:
            mv = min(a, num)
            result += da * mv
            a -= mv

            num -= mv
            result += db * num
            b -= num

    print(result)
    