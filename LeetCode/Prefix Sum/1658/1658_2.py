def solve(nums, x):
    target = sum(nums) - x
    if target == 0:
        return len(nums)

    d = {0 : -1}
    result = -int(1e9)
    
    sumValue = 0

    for idx, value in enumerate(nums):
        sumValue += value
        if sumValue - target in d:
            result = max(result, idx - d[sumValue - target])

        d[sumValue] = idx

    return len(nums) - result if result != -int(1e9) else -1

print(solve([2, 3, 1, 2, 4, 3], 9))