credit = input("Good Credit? ")
price = int(input("House price: "))

if credit == "yes":
    print(price * .1)
else:
    print(price * .2)
