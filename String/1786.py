

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

def kmp(s, p):
    result = []
    pi = getPi(p)
    n, m, j = len(s), len(p), 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == m - 1:
                result.append(i - m + 1)
                j = pi[j]
            else:
                j += 1
                
    return result

s = input()
p = input()
matched = kmp(s, p)
print(len(matched))
for i in matched:
    print(i + 1, end = ' ')
    
