def getPi(p):
    m, j = len(p), 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j

    result = m // (m - pi[-1])
    if m % (m - pi[-1]) == 0: return result
    else: return 1

while True:
    s = input()
    if s[0] == '.': break
    print(getPi(s))