arr = [1,2,3,2,2,3,1,1,2,3]
arr.sort()

for i,n in enumerate(arr):
    if arr.count(n) > 1 :
        arr.pop(i)

print(arr)
print(list(set(arr)))