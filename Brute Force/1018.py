a, b = map(int, input().split())
board = [list(input()) for _ in range(a)]
result = int(1e9)

def check(i, j):
    b, w = 1, 0
    count1, count2 = 0, 0
    color = ['W', 'B']
    for r in range(i, i + 8):
        for c in range(j, j + 8):
            if board[r][c] != color[b]:
                count1 += 1
            if board[r][c] != color[w]:
                count2 += 1
            b ^= 1
            w ^= 1
        b ^= 1
        w ^= 1
    return min(count1, count2)
                
for i in range(a - 8 + 1):
    for j in range(b - 8 + 1):
        result = min(result, check(i, j))
        
print(result)
