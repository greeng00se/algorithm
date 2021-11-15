import sys

input = sys.stdin.readline

t = [[[0] * 21 for i in range(21)] for j in range(21)]
for i in range(0, 21):
    for j in range(0, 21):
        for k in range(0, 21):
            if i == 0 or j == 0 or k == 0:
                t[i][j][k] = 1
            
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                t[i][j][k] = t[i][j][k - 1] + t[i][j - 1][k - 1] - t[i][j - 1][k]
            else:
                t[i][j][k] = t[i - 1][j][k] + t[i - 1][j - 1][k] + t[i - 1][j][k - 1] - t[i - 1][j - 1][k - 1]
    
while True:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break 
    elif a <= 0 or b <= 0 or c <= 0:
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, 1))
    elif a > 20 or b > 20 or c > 20:
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, t[20][20][20]))
    else:
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, t[a][b][c]))