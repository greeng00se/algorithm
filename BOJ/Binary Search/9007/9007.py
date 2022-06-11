import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(4)]

    group1 = []
    group2 = []

    for i in range(n):
        for j in range(n):
            group1.append(data[0][i] + data[1][j])
            group2.append(data[2][i] + data[3][j])

    group1.sort()
    group2.sort()
    result = int(1e9)
    minDiff = int(1e9)

    for v in group1:
        l, r = 0, len(group2) - 1

        while l <= r:
            mid = (l + r) // 2
            s = v + group2[mid]
            diff = abs(k - s)

            if s > k:
                r = mid - 1
            else:
                l = mid + 1

            if minDiff > diff:
                result = s
                minDiff = diff
            elif minDiff == diff:
                result = min(result, s)

    print(result)

                
            

