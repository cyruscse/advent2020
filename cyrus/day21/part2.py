# Advent of Code 2020 Day 21 Part 2 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    allergen_ingredients = dict()
    ingredients = list()
    allergens = list()
    ingredient_set = set()
    allergen_tbd = set()

    for in_line in in_file:
        recipe_ingredients = set()
        recipe_allergens = set()

        for ingredient in in_line.split('(')[0].strip().split(' '):
            recipe_ingredients.add(ingredient)

        for allergen in in_line.split('contains')[1].strip().strip(')').split(','):
            recipe_allergens.add(allergen.lstrip())
            allergen_tbd.add(allergen.lstrip())

        ingredients.append(recipe_ingredients)
        allergens.append(recipe_allergens)

    recipe_idx = 0

    for allergen_set in allergens:
        for allergen in allergen_set:
            if allergen not in allergen_ingredients.keys():
                allergen_ingredients[allergen] = set(ingredients[recipe_idx])
            else:
                allergen_ingredients[allergen] = set(ingredients[recipe_idx]) & allergen_ingredients[allergen]

            for ingredient in allergen_ingredients[allergen]:
                ingredient_set.add(ingredient)
        recipe_idx = recipe_idx + 1
    print(allergen_ingredients)

    verified_allergens = set()

    while len(allergen_tbd):
        allergen_tbd = allergen_tbd - verified_allergens
        for allergen in allergen_tbd:
            if len(allergen_ingredients[allergen]) == 1:
                verified_allergens.add(allergen)
                unique_ingredient = allergen_ingredients[allergen]
                for allergen_search in allergen_ingredients.keys():
                    if allergen == allergen_search:
                        continue

                    if len(allergen_ingredients[allergen] & allergen_ingredients[allergen_search]) > 0:
                        allergen_ingredients[allergen_search] = allergen_ingredients[allergen_search] - allergen_ingredients[allergen]
                ingredient_set.remove(list(unique_ingredient)[0])

                if len(ingredient_set) == len(allergen_ingredients.keys()):
                    break

    allergen_list = list(allergen_ingredients.keys())
    allergen_list = sorted(allergen_list)

    for allergen in allergen_list:
        print('{},'.format(list(allergen_ingredients[allergen])[0]), end='')

main()
