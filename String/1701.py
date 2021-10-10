def getPi(p):
    m, j = len(p), 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j

    return max(pi)

s = input()
result = 0
for i in range(len(s)):
    result = max(getPi(s[i:]), result)
    
print(result)