from bisect import bisect_left

n = int(input())
data = list(map(int,input().split()))
d = [data[0]]
for x in data:
    if d[-1] < x:
        d.append(x)
    else:
        d[bisect_left(d, x)] = x

print(len(d))