import sys
 
input = sys.stdin.readline
 
rep = int(input())
 
for i in range(rep):
    n, m, k = map(int, input().split())
    if k <= 1:
        print('NO')
        continue
    if n == 1:
        if m == 0: print('YES')
        else: print('NO')
        continue
        
    a, b = n - 1, (n * (n - 1)) // 2
    if a <= m <= b and k >= 4: 
        print('YES')
    elif m == b and k >= 3:
        print('YES')
    else:
        print('NO')