from typing import List
from dataclasses import dataclass

@dataclass
class Intake:
    """
    An intake models the key information about the nut.
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


def optimal_calories(options: List[Intake], min_calories: float = 1000, max_calories: float = 3000) -> List[Intake]:
    """
    This algorithm computes, out of a large sequence of 
    foods, the optimal selection that guarantees a number 
    of calories for the minimum price.

    Arguments
    ---------
    options: list of Intake
        List of all possible choices 
    min_calories: float, defaults to 1000
        Minimum amount of calories
    max_calories: float, defaults to 3000
        Maximum amount of calories

    Returns
    -------
    List[Intake]:
        List of intake whose sum of calories are between 
        the minimum and maximum required whilst minimizing 
        the purchase price.
    """    
    return [] 










# class Intake2:

#     # The slots are a construct in python that reserves space
#     # on the memory associated with the object to store these
#     # properties, so they don't have to be looked up in a 
#     # hashmap giving you better memory profile (3x less) and 
#     # faster execution.
#     __slots__ = ('__name', '__calories', '__price')

#     def __init__(self, name: str, calories: float, price: float) -> None:
#         # 2 __ underscores at the begining of a field makes 
#         # the field private, so all the access go through the 
#         # methods below
#         self.__name = name 
#         self.__calories = calories 
#         self.__price = price 

#     @property 
#     def name(self)->str:
#         """Name of the food"""
#         return self.__name 

#     @name.setter
#     def name(self, value: str) -> None: 
#         if len(value) == 0:
#             raise ValueError("Name cannot be an empty string")
#         self.__name = value 

#     @property 
#     def calories(self)->float:
#         return self.__calories 

#     @calories.setter
#     def calories(self, value: float) -> None: 
#         self.__calories = value 

#     @property 
#     def _price(self)->float:
#         return self.__price 

#     @_price.setter
#     def _price(self, value: float) -> None: 
#         self.__price = value 