def solve(arr, k):
    d = {}
    for i in range(len(arr)):
        if k - arr[i] in d:
            return True
        d[arr[i]] = True
    return False
print(solve([10, 15, 3, 7], 17))
