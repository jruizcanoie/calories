from calories import Intake, optimal_calories

# to discover test, we need to call the functions as "test_"
# and the file name has to be in tests directories and 
# it should finish with "_test.py"
def test_optimal_calories():
    foods = [Intake("Apple", 5, 0.5), Intake("Pear", 3, 0.6), Intake("Hamburger", 10000, 2)]
    min_calories = 0 
    max_calories = 10

    result = optimal_calories(foods)

    total_calories = 0
    total_price = 0
    for recomendation in result:
        total_calories += recomendation.calories
        total_price += recomendation.price
    
    assert total_calories > min_calories and total_calories < max_calories



    





