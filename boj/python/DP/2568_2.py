import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()

lp = []
cnt = [-1] * n
for i, v in enumerate(a):
    s, e = v
    if not lp or lp[-1] < e:
        lp.append(e)
        cnt[i] = len(lp) - 1
    else:
        idx = bisect_left(lp, e)
        lp[idx] = e
        cnt[i] = idx
        
ans, c = [], max(cnt)
for i in range(n - 1, -1, -1):
    if cnt[i] == c:
        c -= 1
    else:
        ans.append(a[i][0])

print(len(ans))
print('\n'.join(map(str, reversed(ans))))