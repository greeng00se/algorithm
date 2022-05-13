import sys

input = sys.stdin.readline

def check(depth):
    for i in range(depth):
        if data[depth] == data[i] or abs(data[depth] - data[i]) == abs(depth - i):
            return False

    return True

def bt(depth):
    global result

    if depth >= n:
        result += 1
        return

    for i in range(n):
        data[depth] = i
        if check(depth):
            bt(depth + 1)

n = int(input())
data = [0] * n
result = 0
bt(0)
print(result)