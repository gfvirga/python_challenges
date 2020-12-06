weight_kg = int(input("Enter your Weight: "))
unit = input('(L)bs or (K)gs? ')

if unit.upper() == "L":
    print(f"You weight {.45 * weight_kg} kg")
elif unit.upper()  == "K":
    print("You weight " + str(2.20462 * weight_kg) + " lbs")
else:
    print("You entered wrong type")
