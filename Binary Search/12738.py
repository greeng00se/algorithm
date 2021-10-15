from bisect import bisect_left

n = int(input())
a = list(map(int,input().split()))
d = [a[0]]
for x in a:
    if d[-1] < x:
        d.append(x)
    else:
        d[bisect_left(d, x)] = x

print(len(d))