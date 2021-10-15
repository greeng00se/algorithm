def solve():
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    q = [data[0]]
        
    for i in range(1, n):
        if len(q) == k and min(q) > data[i]:
            return 'NO'
        if len(q) < k and min(q) > data[i]:
            q.append(data[i])
            continue
            
        dif = int(1e9)
        idx = 0
        for j in range(len(q)):
            m = data[i] - q[j]
            if 0 < m < dif:
                dif = m
                idx = j
                
        q[idx] = data[i]
                
    return 'YES'
    
print(solve())