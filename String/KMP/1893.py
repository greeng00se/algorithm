import sys

input = sys.stdin.readline

def getPi(p):
    m, j = len(p), 0
    pi = [0] * (m + 1)
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
            
    return pi

rep = int(input())    
for _ in range(rep):
    result = []
    order = input().rstrip()
    itol = {}
    ltoi = {}
    for i in range(len(order)):
        itol[i] = order[i]
        ltoi[order[i]] = i
                
    plain = list(input().rstrip())
    pi = getPi(plain)
    crypt = input().rstrip()
        
    for i1 in range(len(order)):
        if i1 != 0:
            for j1 in range(len(plain)):
                plain[j1] = itol[(ltoi[plain[j1]] + 1) % len(order)]
        
        s, p = crypt, plain
        cnt = 0
        n, m, j = len(s), len(p), 0
        for i in range(n):
            if cnt >= 2: break
            while j > 0 and s[i] != p[j]:
                j = pi[j - 1]
            if s[i] == p[j]:
                if j == m - 1:
                    cnt += 1
                    j = pi[j]
                else:
                    j += 1

        if cnt == 1:
            result.append(i1)
        
    if not result:
        print('no solution')
    if len(result) >= 2:
        print('ambiguous:', *result)
    if len(result) == 1:
        print('unique:', *result)
        