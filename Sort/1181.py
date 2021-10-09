n = int(input())
arr = list(set([input() for _ in range(n)]))
data = [[] for _ in range(51)]
for w in arr: data[len(w)].append(w)
for i in data:
    if i: print(*sorted(i), sep = '\n')
