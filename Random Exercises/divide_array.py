array = [1,2,3,5,11]
for i in range(1,len(array)):
  if sum(array[:i]) == sum(array[i:]):
    print([array[:i], array[i:]])