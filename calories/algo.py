from typing import List
from dataclasses import dataclass

from calories.ds import (
    load_recipe_recipe_database,
    load_recipe_ingredients_recipe_dataset,
    load_recipe_calories_dataset,
    load_recipe_price_dataset,
    load_recipe_recipe_calories_dataset,
    load_recipe_recipe_ingredients_dataset,
)

recipe_database = load_recipe_recipe_database()

ingredients_recipe_dataset = load_recipe_ingredients_recipe_dataset()

calories_dataset = load_recipe_calories_dataset()

price_dataset = load_recipe_price_dataset()

recipe_ingredients_dataset = load_recipe_recipe_ingredients_dataset()

recipe_calories_dataset = load_recipe_recipe_calories_dataset()


class Fridge:
    """
    This creates a class named Fridge
    Here the user will be able to input thier items that they have in the fridge in order
    To be able to calculate a good meal for them later, based on the items they have.
    """

    def __init__(self):
        self.__fridge_items = {}

    def add_item(self, item, cal):
        self.__fridge_items[item] = cal

    def get_items_key(self):
        return tuple(self.__fridge_items.keys())

    def max_cal_item(self):
        return max(self.__fridge_items, key=self.__fridge_items.get)

    def max_cal_cal(self):
        return max(self.__fridge_items.values())


@dataclass
class ShopItem:
    """
    An intake models the key information about the nutritional values
    values of an option on a diet.

    It is modeled as a data class since there is no more
    logic than the actual values we are interested from
    the prespective of the algorithm.
    """

    name: str
    """Name of the food"""
    calories: float
    """Amount of calories"""
    price: float
    """Price of the item"""


def find_recipe(user_fridge):
    """
    Given the items inside of the users fridge, we find the one with the most calories
    If it doesnt pass a condition, we go to the grocery store (TO be continued)

    If it does, we then check against the ingredients_recipe_dataset to find the recepies
    that can be made with the ingredient

    Args:
        user_fridge
            contains the items inside the fridge

    Returns:
        recipes
            contains the recipes which can be cooked with the ingredient
    """
    max_fridge = user_fridge.max_cal_cal()
    max_fridge = float(max_fridge)

    if max_fridge < 100:
        print("Find item from grocery store ")

    max_fridge = user_fridge.max_cal_item()

    if max_fridge in ingredients_recipe_dataset:
        value = ingredients_recipe_dataset[max_fridge]
    return value


def mostcom(reference, tocheck):
    """
    This function finds the commonalities between the two inputted lists
    It will return the recepies with the most common items inside of the fridge
    This is done to use as many fridge items as possible
    """
    max_common = 0
    common_lists = []
    for sublist in tocheck:
        num_common = sum(1 for element in sublist if element in reference)
        if num_common > max_common:
            max_common = num_common
            common_lists = [sublist]
        elif num_common == max_common:
            common_lists.append(sublist)
    return common_lists


def recipe_breakdown(recipes):
    """
    Accesses the recepies dictionary so the recipies are able to be broken down
    """
    all_ingredients = []
    for i in recipes:
        if i in recipe_ingredients_dataset:
            all_ingredients.append(recipe_ingredients_dataset[i])
    return all_ingredients


def fridge_op(fridge):

    test = 0
    while test == 0:

        answer = (
            input("Would you like to add an item into your fridge? (y/n) ")
            .strip()
            .lower()
        )

        if answer == "y" or answer == "n":
            test = 1
        else:
            print(
                "Please only enter either 'y' or 'n'. No other inputs will be accepted"
            )

    while answer == "y":

        food_name = (
            input("What item would you like to add: (eg: banana) ").strip().lower()
        )

        if any(character.isdigit() for character in food_name):
            print(
                "Invalid input. Item deleted. Please do not enter numbers or any special symbols!"
            )
            continue

        food_calorie = input("How many calories does the item contain: (eg: 100)")

        try:
            food_calorie_float = float(food_calorie)
        except ValueError:
            print(
                "Invalid input. Item deleted. Please make sure that only numbers are placed when the program asks for calories!"
            )
            continue

        answer2 = input(
            f"You want to add {food_name} which has {food_calorie} calories to the fridge? Is this correct? y/n "
        )

        if answer2 == "y":
            fridge.add_item(food_name, food_calorie)
            print("Item added! ")

            answer = input("Would you like to add an item into your fridge? y/n ")

        else:
            print("Item deleted.")
            answer = input("Would you like to add an item into your fridge? y/n ")

    c = fridge.get_items_key()

    print("These are the items inside of your fridge\n", c)

    cookyes = input("Are you ready to start cooking? y/n ")

    if cookyes == "y":
        pass
    else:
        fridge_op(fridge)


def beststringmatch(commonlists, recipes):
    """
    Finds the best match between ingredients and the recepies
    """
    matching_keys = []

    for recipe in recipes:
        if recipe in recipe_ingredients_dataset:
            recipe_ingredients = set(recipe_ingredients_dataset[recipe])
            for commonlist in commonlists:
                if recipe_ingredients.issuperset(commonlist):
                    matching_keys.append(recipe)
                    break

    if not matching_keys:
        max_common = 0
        best_match = None
        for recipe in recipes:
            if recipe in recipe_ingredients_dataset:
                recipe_ingredients = set(recipe_ingredients_dataset[recipe])
                common_count = len(recipe_ingredients.intersection(commonlists))
                if common_count > max_common:
                    max_common = common_count
                    best_match = recipe
        if best_match:
            matching_keys.append(best_match)

    return matching_keys


def checkitems(recipe, fridge):
    """
    Finds the most efficient use of the fridge
    If there is a clash of ingredients, the most efficient calorie price is calculated
    and the one that uses those ingredients is the one shown to the user.
    """

    tupleitems = fridge.get_items_key()

    totalprice = []
    totalcal = []

    for i in recipe:

        condition = True

        missing_values = []

        x = recipe_ingredients_dataset[i]
        for y in x:
            if y not in tupleitems:
                condition = False
                missing_values.append(y)

        if condition is True:
            return f"You have all the items for {i}"

        else:
            semi_price = 0
            semi_cal = 0
            for item in missing_values:

                semi_price += price_dataset[item]
                semi_cal += calories_dataset[item]
            totalprice.append(semi_price)
            totalcal.append(semi_cal)

    efficientlist = []
    for i in range(len(recipe)):
        totalpriceitem = totalprice[i]
        totalcalitem = totalcal[i]
        efficient = totalcalitem / totalpriceitem
        efficientlist.append(efficient)

    maxeff = max(efficientlist)
    maxeff_index = efficientlist.index(maxeff)

    z = recipe[maxeff_index]
    missing_val = []
    xx = recipe_ingredients_dataset[z]
    for finaltest in xx:
        if finaltest not in tupleitems:
            missing_val.append(finaltest)

    return f"You should cook {recipe[maxeff_index]}. However, you are missing {missing_val}. This will cost you {totalprice[maxeff_index]} euros"


def main():

    f = Fridge()

    fridge_op(f)

    x = find_recipe(f)

    z = recipe_breakdown(x)

    y = f.get_items_key()

    c = mostcom(y, z)

    test = beststringmatch(c, x)

    final = checkitems(test, f)

    print(final)
