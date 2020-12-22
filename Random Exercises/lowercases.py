s = "A man, a plan, a canal: Panama"
joined_s = ''
for char in s:
    if char.isalnum():
        joined_s += char.lower()

print(joined_s)


print(''.join(char for char in s if char.isalnum()).lower())