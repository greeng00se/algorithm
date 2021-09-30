n = int(input())
result = 1
a, b, i = 1, 1, 1
if n == 1: print(1)
else:
    while True:
        b += i * 6
        result += 1
        if a <= n <=b:
            print(result)
            break
        i += 1
        a = b