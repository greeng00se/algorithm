n = int(input())

def solve(s, e, p, n):
    if n == 1:
        print(s, e)
        return
    
    solve(s, p, e, n - 1)
    print(s, e)
    solve(p, e, s, n - 1)

print(2 ** n - 1)
solve(1, 3, 2, n)