
def getTrappedRainWater(arr):
  max_level = []
  top = 0
  for h in arr:
    if h > top:
      top = h
    max_level.append(top)
  top = 0
  for i in reversed(range(len(arr))):
    if arr[i] > top:
      top = arr[i]
    max_level[i] = min(max_level[i],top)

  for i in range(len(arr)):
    max_level[i] = max_level[i] - arr[i]

  return sum(max_level)
  

print(getTrappedRainWater([6,9,9]))