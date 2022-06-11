def getPi(p):
    j = 0
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j

def kmp(s, p):
    result = 0
    getPi(p)
    n, m, j = len(s), len(p), 0
    flag = False
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == m - 1:
                result += 1
                j = pi[j]
            else:
                j += 1
    return result

n = int(input())
arr1 = list(input().split())
arr2 = list(input().split())
arr1 = arr1 * 2
pi = [0] * n
flag = True
for i in range(len(arr2)):
    if arr2[i] != arr1[i]:
        flag = False
    
a, b = kmp(arr1, arr2), n
if flag: a -= 1
if b % a == 0:
    a, b = a // a, b // a
print(a, '/', b, sep = '')
