def findDuplicates(arr):
  # Write your code here
  dups = set()
  
  for i, n in enumerate(arr):
    if n in arr[i+1:]:
      dups.add(n)

  return [x for x in dups]

print(findDuplicates([2,3,1,2,3]))