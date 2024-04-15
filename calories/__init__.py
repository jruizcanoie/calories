from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('calories')
except PackageNotFoundError:
    __version__ = '(local)'

del PackageNotFoundError
del version

# We want the users of this library to use these 
# types and function, whilst we may want to hide 
# others which are not part of the public inteface
# of this library

# From algo file, we want to export the following functions

from .algo import Fridge, ShopItem, find_recipe, mostcom, recipe_breakdown, fridge_op, beststringmatch, checkitems

#from .ds import load_recipe_recipe_database,load_recipe_ingredients_recipe_dataset,load_recipe_calories_dataset,load_recipe_price_dataset,load_recipe_recipe_calories_dataset,load_recipe_recipe_ingredients_dataset

from . import ds

# if the user of this library imports this library 
# with `from calories import *`, the following list 
# will be the only public classes and function the 
# user will be able to see.
__all__ = ["ds","Fridge", "ShopItem", "find_recipe", "mostcom", "recipe_breakdown", "fridge_op", "beststringmatch", "checkitems"]
