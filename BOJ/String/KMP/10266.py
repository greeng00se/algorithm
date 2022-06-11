def getPi(p):
    j = 0
    for i in range(1, N):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j

def kmp(s, p):
    result = []
    getPi(p)
    n, m, j = len(s), len(p), 0
    flag = False
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == m - 1:
                flag = True
                break
            else:
                j += 1
    if flag: print('possible')
    else: print('impossible')
    return result

N = 360000
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

clock1 = [0] * (N * 2)
clock2 = [0] * N
pi = [0] * N

for time in arr1:
    clock1[time] = 1
    clock1[N + time] = 1
    
for time in arr2:
    clock2[time] = 1
    
kmp(clock1, clock2)