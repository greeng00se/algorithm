matrix = [[i * j for i in range(1, 11)] for j in range(1, 11)]

minValue = min(map(min, matrix))
maxValue = max(map(max, matrix))

print(minValue, maxValue)