n,k,*d=map(int,open(0).read().split())
d.sort()
print(sum(sorted([d[i+1]-d[i]for i in range(n-1)])[:n-k]))