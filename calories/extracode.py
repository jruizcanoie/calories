
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







# class Recepies(): 

#     def __init__(self, cooked: str, itemneed: str, totalcal: float):
#         self.__cooked = cooked 
#         self.__itemneed = itemneed 
#         self.__totalcal = totalcal 







# @dataclass
# class Fridge: 
#     """
#     This creates an object called Fridge. Users can add items into their fridge. 
    
#     Using this information, we can create meals based on the food they already have 
#     to stop them from buying more food they do not need. 
#     """
#     foodname: str 
#     """Name of food"""
#     quantity: float
#     """Quantity of item"""
#     calories: float 
#     """Calories of the item"""