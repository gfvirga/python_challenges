file = open('./inputs/day21input.txt',mode='r')
labels = [e.replace(")","").split(" (contains ") for e in file.read().split("\n")]

allergens = {}
# Create a dict with the possible ingredients for each allergen:
# {'dairy': ['mxmxvkd'], 'fish': ['sqjhc', 'mxmxvkd'], 'soy': ['sqjhc', 'fvjkl']}
occurrences = {}
# Count how many times each ingredient appears
# {'mxmxvkd': 3, 'kfcds': 1, 'sqjhc': 3, 'nhms': 1, 'trh': 1, 'fvjkl': 2, 'sbzzf': 2}
for label in labels:
    for allergen in label[1].split(', '):
        if allergen in allergens:
            allergens[allergen] = [i for i in label[0].split(' ') if i in allergens[allergen]]
        else:
            allergens[allergen] = [ i for i in label[0].split(' ')]
    for ingredient in label[0].split(' '):
        if ingredient in occurrences:
            occurrences[ingredient] += 1
        else:
            occurrences[ingredient] = 1

# Count how many time an ingredient is not possible in an allergen use occurences to keep track of times.
count = 0
for ingredient, times in occurrences.items():
    if all(ingredient not in v for v in allergens.values()):
        count += times

# Clean allergens that are unique
used = set()
while any(len(a) > 1 for a in allergens.values()):
    for allergen, ingredient in allergens.items():
        if len(ingredient) == 1 and ingredient[0] not in used:
            used.add(ingredient[0])
        elif len(ingredient) > 1:
            for i in used:
                if i in ingredient:
                    allergens[allergen].remove(i)

# Sort allergens alphabetically and add ingredient to string.
ingredients = ','.join(v[0] for k,v in sorted(allergens.items(), key= lambda k:k[0] ) )

print(f"Part One: {count}")
print(f"Part Two: {ingredients}")