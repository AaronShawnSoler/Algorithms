#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # get recipe keys
    recipeKeys = recipe.keys()
    # get max batch for each ingredient for each key
    maxBatch = [0] * len(recipeKeys)
    for index, key in enumerate(recipeKeys):
        if key in ingredients:
            maxBatch[index] = ingredients[key] // recipe[key]
    # return min batches for some ingredient
    return min(maxBatch)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
