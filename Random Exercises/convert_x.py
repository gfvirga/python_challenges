numbers = [5,2,5,2,2]

for number in numbers:
    print("x" * number)

for number in numbers:
    res = ""
    for count in range(number):
        res += 'x'
    print(res)