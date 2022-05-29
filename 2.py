import functools
def solve(arr):
  res = []
  p = functools.reduce(lambda x, y: x * y, arr)
  for i in arr:
      res.append(p / i)
  return(res)
  
solve([1, 2, 3, 4, 5])
