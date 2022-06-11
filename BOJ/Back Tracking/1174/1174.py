import sys

input = sys.stdin.readline

def bt(now, start):
    
    if len(now) > 10:
        return

    numbers.append(int(now))

    for i in range(start - 1, -1, -1):
        bt(now + str(i), i)

n = int(input())
numbers = []
for i in range(10):
    bt(str(i), i)

numbers.sort()
print(-1 if n > len(numbers) else numbers[n - 1])