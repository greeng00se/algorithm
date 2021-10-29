import sys

input = sys.stdin.readline

MOD = int(1e9) + 7
n = int(input())
f = {}

def fibo(n):
    if n <= 0: return 0
    if 1 <= n <= 2: return 1
    if n in f.keys(): return f[n]
    
    if n % 2 == 1:
        m = (n + 1) // 2
        t1 = fibo(m)
        t2 = fibo(m - 1)
        f[n] = t1 * t1 + t2 * t2
        f[n] %= MOD
        return f[n]
    if n % 2 == 0:
        m = n // 2
        t1 = fibo(m - 1)
        t2 = fibo(m)
        f[n] = (2 * t1 + t2) * t2;
        f[n] %= MOD
        return f[n];
    
print(fibo(n) % MOD)

