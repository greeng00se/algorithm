import sys

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    n = int(input())
    if n % 25 == 0:
        print(0)
        continue
        
    result = 0
    flag = 0
    a = ''
    b = str(n)
    i = len(b) - 1
    
    while i >= 0:
        if b[i] in ['0', '2', '5', '7']: a += b[i]
        else: result += 1
            
        for j in range(0, len(a)):
            for k in range(j + 1, len(a)):
                if flag == 1: break
                c = a[j] + a[k]
                if c in ['00', '52', '05', '57']:
                    flag = 1
                    result += len(a) - 2
                
        if flag: break
            
        i -= 1
        
    print(result)
        
        