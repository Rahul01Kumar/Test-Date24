array_nums = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)

print(result)
