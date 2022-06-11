# nCr = n!/(n-r)!r!

n, m = map(int, input().split())

def countN(n, m, k):
    return count(n, k) - count(n - m, k) - count(m, k)
    
def count(n, k):
    result = 0
    while n:
        n //= k
        result += n
    return result

print(min(countN(n, m, 2), countN(n, m, 5)))