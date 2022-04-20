import sys

input = sys.stdin.readline

n = int(input())
t = int(input())

MAX = n * 2 + 1
MAX_VALUE = int(1e18)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solve():
    d = 1
    result = 0
    lines = []

    r, c = n, n
    for i in range(t + 1):
        count = MAX_VALUE
        if i != t:
            a, b = input().rstrip().split()
            count = int(a)
        
        nr = r + dr[d] * count
        nc = c + dc[d] * count

        v = MAX_VALUE
        if (nr < 0): v = min(v, r + 1)
        if (nr >= MAX): v = min(v, MAX - r)
        if (nc < 0): v = min(v, c + 1)
        if (nc >= MAX): v = min(v, MAX - c)


        for i in range(len(lines) - 1):
            sr, sc = lines[i][0]
            er, ec = lines[i][1]

            isVerticlaLine = sc == ec

            if d == 0:
                if isVerticlaLine and nr <= er < r and sc == nc:
                    v = min(v, r - er)
                if not isVerticlaLine and sc <= nc <= ec and nr <= er < r:
                    v = min(v, r - er)
            if d == 1:
                if isVerticlaLine and sr <= nr <= er and c < sc <= nc:
                    v = min(v, sc - c)
                if not isVerticlaLine and c < sc <= nc and sr == nr:
                    v = min(v, sc - c)
            if d == 2:
                if isVerticlaLine and r < sr <= nr and sc == nc:
                    v = min(v, sr - r)
                if not isVerticlaLine and sc <= nc <= ec and r < sr <= nr:
                    v = min(v, sr - r)
            if d == 3:
                if isVerticlaLine and sr <= nr <= er and nc <= ec < c:
                    v = min(v, c - ec)
                if not isVerticlaLine and nc <= ec < c and sr == nr:
                    v = min(v, c - ec)

        if v != MAX_VALUE:
            return result + v

        lines.append(sorted([[r, c], [nr, nc]]))
        r, c = nr, nc
        result += count
        d = (d + (3 if b == 'L' else 1)) % 4

    return result

print(solve())