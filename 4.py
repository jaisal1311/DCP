def solve(arr):
    arr = list(filter(lambda x: x > 0, sorted(arr)))
    n = max(arr)
    o_sum = ((n * n) + n) / 2
    a_sum = sum(arr)
    if o_sum == a_sum:
        return n + 1
    else:
        return abs(o_sum - a_sum)

print(solve([3, 4, -1, 1]))
