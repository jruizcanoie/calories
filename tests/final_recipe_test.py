from calories import Fridge, ShopItem, find_recipe, mostcom, recipe_breakdown, fridge_op, beststringmatch, checkitems, load_recipe

# to discover test, we need to call the functions as "test_"
# and the file name has to be in tests directories and 
# it should finish with "_test.py"

def test_recipe():
   load_recipe()
   f = Fridge()
   fridge_op(f)
   x = find_recipe(f)
   z= recipe_breakdown(x)
   y = f.get_items_key()
   c = mostcom(y,z)
   test = beststringmatch(c , x)
   checkitems(test,f) 


test_recipe()




    





