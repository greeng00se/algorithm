matrix = [[i * j for i in range(1, 4)] for j in range(1, 4)]
print(*matrix, sep = '\n')
print()

# spin left
left = [list(t[::-1]) for t in zip(*matrix[::-1])][::-1]
print(*left, sep = '\n')
print()

# spin right
right = [list(t) for t in zip(*matrix[::-1])]
print(*right, sep = '\n')