# Advent of Code 2020 Day 21 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    ingredient_allergens = dict()
    ingredients = list()
    poisoned = set()
    good_ingredients = 0

    for in_line in in_file:
        recipe_ingredients = set()
        recipe_allergens = set()

        for ingredient in in_line.split('(')[0].strip().split(' '):
            recipe_ingredients.add(ingredient)
            ingredients.append(ingredient)

        for allergen in in_line.split('contains')[1].strip().strip(')').split(','):
            recipe_allergens.add(allergen.lstrip())

        for allergen in recipe_allergens:
            if allergen not in ingredient_allergens.keys():
                ingredient_allergens[allergen] = recipe_ingredients
            else:
                ingredient_allergens[allergen] = recipe_ingredients & ingredient_allergens[allergen]

    for allergen in ingredient_allergens.keys():
        for ingredient in ingredient_allergens[allergen]:
            poisoned.add(ingredient)

    for ingredient in ingredients:
        if ingredient not in poisoned:
            good_ingredients = good_ingredients + 1

    print(good_ingredients)

main()
