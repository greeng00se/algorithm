while True:
    n = int(input())
    if n == 0: break
    if str(n) == str(n)[::-1]: print('yes')
    else: print('no')