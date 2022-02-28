import sys
from itertools import chain

input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]
moderator = [list(map(int, input().split())) for _ in range(5)]
moderator = list(chain(*moderator))

result = 0

def check():
    result = 0
    diaA = diaB = 0
    spin = [list(t) for t in zip(*bingo[::-1])]
    
    for i in range(5):
        if bingo[i] == [0] * 5:
            result += 1
        if spin[i] == [0] * 5:
            result += 1
        
        if bingo[i][i] == 0: diaA += 1
        if spin[i][i] == 0: diaB += 1

    if diaA == 5: result += 1
    if diaB == 5: result += 1

    if result >= 3: return 1
    else: 0
    
for number in moderator:
    result += 1

    for r in range(5):
        for c in range(5):
            if bingo[r][c] == number:
                bingo[r][c] = 0

    if check():
        print(result)
        break


