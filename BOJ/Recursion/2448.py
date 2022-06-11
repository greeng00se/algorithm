n = int(input())
star = [[' '] * (n * 2 - 1) for _ in range(n)]

def s(h, w, x):
    if x == 3:
        for r, c in zip('011', '213'):
            star[h + int(r)][w + int(c)] = '*'
        for i in range(5): star[h + 2][w + i] = '*'
    else:
        s(h, w + x // 2, x // 2)
        s(h + x // 2, w, x // 2)
        s(h + x // 2, w + x, x // 2)
        
s(0, 0, n)
for i in star:
    print(''.join(i))
        