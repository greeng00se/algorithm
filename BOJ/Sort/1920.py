from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))
for x in b:
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x: print(1)
    else: print(0)
    