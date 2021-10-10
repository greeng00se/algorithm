def getPi(s):
    n, j = len(s), 0
    pi = [0] * n
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    
    return pi
            
    
def kmp(s1, s2):
    n, m, j = len(s1), len(s2), 0
    pi = getPi(s2)
    flag = 0
    for i in range(n):
        while j > 0 and s1[i] != s2[j]:
            j = pi[j - 1]
        if s1[i] == s2[j]:
            if j == m - 1:
                flag = 1
                break
                j = pi[j]
            else:
                j += 1
    return flag
                
a = input()
b = input()
print(kmp(a, b))