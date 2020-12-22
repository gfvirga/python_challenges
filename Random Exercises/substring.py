s = "aaaagfffffdafdd"
k = 3
array = []

substring_helper = s[0]
for char in s[1:]:
    if char in substring_helper:
        substring_helper += char
    else:
        array.append(substring_helper)
        substring_helper = char
if substring_helper:
    array.append(substring_helper)


array.sort(key=lambda x:len(x), reverse=True)

print(array[:k])