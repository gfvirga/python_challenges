def countPairs(arr, k):
  # Write your code here
  pairs = 0
  left = 0
  right = len(arr)-1
  while left < right:
    sum = arr[left]+arr[right] 
    print(sum)
    if sum == k:
      pairs += 1
      left += 1
      right -= 1
    elif sum < k:
      left += 1
    elif sum > k:
      right -= 1
  
  return pairs

print(countPairs([1, 2, 3, 4, 5, 6, 7], 8))