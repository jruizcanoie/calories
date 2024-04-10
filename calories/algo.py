from typing import List
from dataclasses import dataclass
recipe_database = {
"Spaghetti Bolognese": {
        "ingredients": ["spaghetti", "tomato sauce", "ground beef", "onion", "garlic"],
        "calories": 600
    },
    "Caesar Salad": {
        "ingredients": ["romaine lettuce", "croutons", "parmesan cheese", "caesar dressing"],
        "calories": 350
    },
    "Grilled Cheese Sandwich": {
        "ingredients": ["bread", "cheese", "butter"],
        "calories": 400
    },
    "Chicken Curry": {
        "ingredients": ["chicken", "onion", "garlic", "ginger", "tomato", "curry powder", "coconut milk", "rice"],
        "calories": 700
    },
    "Vegetable Stir Fry": {
        "ingredients": ["broccoli", "bell pepper", "carrot", "onion", "garlic", "soy sauce", "sesame oil"],
        "calories": 300
    },
    "Pasta Primavera": {
        "ingredients": ["pasta", "zucchini", "bell pepper", "tomato", "onion", "garlic", "olive oil", "parmesan cheese"],
        "calories": 450
    },
    "Beef Stew": {
        "ingredients": ["beef", "potato", "carrot", "onion", "celery", "beef broth", "tomato paste", "flour"],
        "calories": 550
    },
    "Fish Tacos": {
        "ingredients": ["fish fillet", "tortillas", "cabbage", "lime", "sour cream", "avocado", "cilantro"],
        "calories": 400
    },
    "Eggplant Parmesan": {
        "ingredients": ["eggplant", "bread crumbs", "tomato sauce", "mozzarella cheese", "parmesan cheese", "olive oil"],
        "calories": 450
    },
    "Spinach and Feta Stuffed Chicken": {
        "ingredients": ["chicken breast", "spinach", "feta cheese", "garlic", "olive oil"],
        "calories": 350
    },
    "Mushroom Risotto": {
        "ingredients": ["arborio rice", "mushrooms", "onion", "garlic", "white wine", "parmesan cheese", "butter"],
        "calories": 500
    },
    "Beef and Broccoli": {
        "ingredients": ["beef", "broccoli", "garlic", "soy sauce", "brown sugar", "cornstarch", "sesame oil"],
        "calories": 450
    },
    "Tomato Basil Soup": {
        "ingredients": ["tomato", "onion", "garlic", "tomato paste", "vegetable broth", "cream", "basil", "olive oil"],
        "calories": 250
    },
    "Chicken Alfredo": {
        "ingredients": ["chicken", "fettuccine", "heavy cream", "parmesan cheese", "butter", "garlic"],
        "calories": 800
    },
    "Shrimp Scampi": {
        "ingredients": ["shrimp", "linguine", "butter", "garlic", "lemon", "white wine", "parsley"],
        "calories": 500
    },
    "Beef Tacos": {
        "ingredients": ["ground beef", "tortillas", "lettuce", "tomato", "cheddar cheese", "salsa", "avocado"],
        "calories": 550
    },
    "Chicken Enchiladas": {
        "ingredients": ["chicken", "tortillas", "enchilada sauce", "cheddar cheese", "onion", "sour cream"],
        "calories": 600
    },
    "Lentil Soup": {
        "ingredients": ["lentils", "carrot", "celery", "onion", "garlic", "vegetable broth", "tomato", "cumin"],
        "calories": 300
    },
    "Margarita Pizza": {
        "ingredients": ["pizza dough", "tomato sauce", "mozzarella cheese", "basil", "olive oil"],
        "calories": 600
    },
    "Beef Chili": {
        "ingredients": ["ground beef", "kidney beans", "tomato", "onion", "garlic", "chili powder", "cumin"],
        "calories": 500
    },
    "Chicken Noodle Soup": {
        "ingredients": ["chicken", "egg noodles", "carrot", "celery", "onion", "garlic", "chicken broth"],
        "calories": 350
    },
    "Beef and Mushroom Pie": {
        "ingredients": ["beef", "mushrooms", "onion", "garlic", "beef broth", "puff pastry"],
        "calories": 600
    },
    "Vegetarian Chili": {
        "ingredients": ["beans", "tomato", "onion", "bell pepper", "corn", "chili powder", "cumin"],
        "calories": 400
    },
    "Tuna Salad": {
        "ingredients": ["canned tuna", "mayonnaise", "celery", "onion", "pickle", "lettuce", "bread"],
        "calories": 350
    },
    "Pancakes": {
        "ingredients": ["flour", "milk", "egg", "baking powder", "sugar", "butter", "maple syrup"],
        "calories": 250
    },
    "French Toast": {
        "ingredients": ["bread", "egg", "milk", "cinnamon", "butter", "maple syrup"],
        "calories": 300
    },
    "Banana Bread": {
        "ingredients": ["flour", "banana", "sugar", "egg", "butter", "baking soda"],
        "calories": 350
    },
    "Omelette": {
        "ingredients": ["egg", "milk", "cheese", "bell pepper", "onion", "mushroom", "butter"],
        "calories": 400
    },
    "Fruit Smoothie": {
        "ingredients": ["banana", "strawberry", "yogurt", "milk", "honey"],
        "calories": 200
    },
    "Greek Salad": {
        "ingredients": ["lettuce", "tomato", "cucumber", "red onion", "feta cheese", "olive oil", "lemon juice"],
        "calories": 300
    },
    "Ratatouille": {
        "ingredients": ["eggplant", "zucchini", "bell pepper", "onion", "tomato", "garlic", "herbs de Provence"],
        "calories": 250
    },
    "Beef Bourguignon": {
        "ingredients": ["beef", "carrot", "onion", "garlic", "red wine", "beef broth", "mushrooms", "bacon"],
        "calories": 700
    },
    "Fettuccine Alfredo": {
        "ingredients": ["fettuccine", "heavy cream", "butter", "parmesan cheese", "garlic"],
        "calories": 750
    },
    "Stuffed Bell Peppers": {
        "ingredients": ["bell pepper", "ground beef", "rice", "onion", "tomato sauce", "cheese"],
        "calories": 400
    },
    "Tiramisu": {
        "ingredients": ["ladyfingers", "coffee", "mascarpone cheese", "eggs", "sugar", "cocoa powder"],
        "calories": 500
    },
    "Chocolate Chip Cookies": {
        "ingredients": ["flour", "butter", "sugar", "brown sugar", "egg", "vanilla extract", "chocolate chips"],
        "calories": 150
    },
    "Creme Brulee": {
        "ingredients": ["heavy cream", "egg yolk", "sugar", "vanilla extract"],
        "calories": 400
    },
    "Beef Wellington": {
        "ingredients": ["beef fillet", "puff pastry", "mushrooms", "onion", "mustard", "egg"],
        "calories": 800
    },
    "Lobster Bisque": {
        "ingredients": ["lobster", "butter", "flour", "heavy cream", "lobster stock", "sherry"],
        "calories": 600
    },
    "Paella": {
        "ingredients": ["rice", "chicken", "chorizo", "shrimp", "bell pepper", "onion", "tomato", "saffron"],
        "calories": 700
    },
    "Tandoori Chicken": {
        "ingredients": ["chicken", "yogurt", "ginger", "garlic", "lemon", "spices"],
        "calories": 450
    },
    "Sushi Rolls": {
        "ingredients": ["sushi rice", "nori", "fish", "vegetables", "soy sauce", "wasabi", "ginger"],
        "calories": 400
    },
    "Beef Pho": {
        "ingredients": ["beef", "rice noodles", "beef broth", "onion", "ginger", "spices", "herbs"],
        "calories": 600
    },
    "Pulled Pork Sandwiches": {
        "ingredients": ["pork shoulder", "bbq sauce", "hamburger buns", "coleslaw"],
        "calories": 500
    },
    "Quiche Lorraine": {
        "ingredients": ["pie crust", "bacon", "cheese", "eggs", "cream", "onion"],
        "calories": 450
    },
    "Tacos al Pastor": {
        "ingredients": ["pork", "pineapple", "onion", "cilantro", "lime", "tortillas"],
        "calories": 400
    },
    "Baklava": {
        "ingredients": ["phyllo dough", "nuts", "sugar", "butter", "honey", "spices"],
        "calories": 350
    },
    "Pad Thai": {
        "ingredients": ["rice noodles", "shrimp", "tofu", "bean sprouts", "peanuts", "egg", "tamarind", "fish sauce"],
        "calories": 500
    },
    "Beef Bulgogi": {
        "ingredients": ["beef", "soy sauce", "sesame oil", "garlic", "ginger", "brown sugar", "green onions"],
        "calories": 600
    },
    "Chicken Shawarma": {
        "ingredients": ["chicken", "yogurt", "lemon", "garlic", "spices", "pita bread", "tahini sauce"],
        "calories": 450
    },
    "Miso Soup": {
        "ingredients": ["dashi", "miso paste", "tofu", "green onions", "seaweed"],
        "calories": 150
    },
    "Ramen": {
        "ingredients": ["ramen noodles", "broth", "chashu pork", "egg", "green onions", "bamboo shoots", "nori"],
        "calories": 400
    },
    "Key Lime Pie": {
        "ingredients": ["graham cracker crust", "sweetened condensed milk", "key lime juice", "egg yolks", "whipped cream"],
        "calories": 350
    }}

ingredients_recipe_dataset = {
    "arborio rice": ["Mushroom Risotto"],
    "avocado": ["Fish Tacos", "Beef Tacos", "Tacos al Pastor"],
    "bacon": ["Quiche Lorraine"],
    "basil": ["Margarita Pizza", "Tomato Basil Soup"],
    "beans": ["Vegetarian Chili"],
    "beef": ["Beef Stew", "Beef and Mushroom Pie", "Beef Bourguignon", "Beef Pho", "Beef Bulgogi"],
    "beef broth": ["Beef Stew", "Beef and Mushroom Pie", "Beef Bourguignon"],
    "beef fillet": ["Beef Wellington"],
    "bell pepper": ["Vegetable Stir Fry", "Pasta Primavera", "Beef and Broccoli", "Beef Bourguignon", "Paella", "Tacos al Pastor"],
    "bread": ["Grilled Cheese Sandwich", "Beef and Mushroom Pie", "Pancakes", "French Toast", "Banana Bread"],
    "broccoli": ["Vegetable Stir Fry", "Beef and Broccoli"],
    "brown sugar": ["Beef and Broccoli"],
    "butter": ["Grilled Cheese Sandwich", "Mushroom Risotto", "Pancakes", "French Toast", "Banana Bread", "Omelette"],
    "cabbage": ["Fish Tacos"],
    "caesar dressing": ["Caesar Salad"],
    "carrot": ["Vegetable Stir Fry", "Beef Stew", "Lentil Soup", "Beef and Mushroom Pie", "Chicken Noodle Soup"],
    "celery": ["Beef Stew", "Lentil Soup", "Chicken Noodle Soup"],
    "cheddar cheese": ["Beef Tacos", "Chicken Enchiladas"],
    "cheese": ["Grilled Cheese Sandwich", "Spinach and Feta Stuffed Chicken", "Mushroom Risotto", "Omelette"],
    "chicken": ["Chicken Curry", "Spinach and Feta Stuffed Chicken", "Chicken Alfredo", "Chicken Enchiladas", "Chicken Noodle Soup", "Chicken Bourguignon", "Tandoori Chicken", "Chicken Shawarma"],
    "chicken broth": ["Chicken Noodle Soup"],
    "chili powder": ["Beef Chili"],
    "chives": ["Potato Soup"],
    "chocolate chips": ["Chocolate Chip Cookies"],
    "cilantro": ["Fish Tacos", "Tacos al Pastor"],
    "cinnamon": ["French Toast"],
    "coleslaw": ["Pulled Pork Sandwiches"],
    "corn": ["Vegetarian Chili"],
    "cornstarch": ["Beef and Broccoli"],
    "cream": ["Tomato Basil Soup", "Creme Brulee"],
    "croutons": ["Caesar Salad"],
    "cucumber": ["Greek Salad"],
    "dashi": ["Miso Soup"],
    "egg": ["Pancakes", "French Toast", "Banana Bread", "Omelette", "Chocolate Chip Cookies"],
    "egg noodles": ["Chicken Noodle Soup"],
    "eggplant": ["Eggplant Parmesan", "Ratatouille"],
    "eggs": ["Quiche Lorraine"],
    "feta cheese": ["Spinach and Feta Stuffed Chicken", "Greek Salad"],
    "fettuccine": ["Chicken Alfredo", "Fettuccine Alfredo"],
    "fish": ["Sushi Rolls"],
    "fish fillet": ["Fish Tacos"],
    "flour": ["Beef Stew", "Beef and Mushroom Pie", "Pancakes", "Banana Bread", "Chocolate Chip Cookies"],
    "garlic": ["Spaghetti Bolognese", "Chicken Curry", "Vegetable Stir Fry", "Pasta Primavera", "Beef Stew", "Tomato Basil Soup", "Eggplant Parmesan", "Spinach and Feta Stuffed Chicken", "Mushroom Risotto", "Beef and Broccoli", "Chicken Alfredo", "Shrimp Scampi", "Chicken Noodle Soup", "Beef and Mushroom Pie", "Beef Bourguignon", "Fettuccine Alfredo", "Tacos al Pastor", "Pad Thai", "Chicken Shawarma", "Miso Soup"],
    "ginger": ["Chicken Curry", "Mushroom Risotto", "Tandoori Chicken", "Chicken Shawarma", "Beef Pho"],
    "graham cracker crust": ["Key Lime Pie"],
    "green onions": ["Beef Pho", "Beef Bulgogi", "Ramen", "Gyoza"],
    "ground beef": ["Spaghetti Bolognese", "Beef Tacos"],
    "heavy cream": ["Chicken Alfredo", "Fettuccine Alfredo", "Creme Brulee"],
    "honey": ["Fruit Smoothie"],
    "key lime juice": ["Key Lime Pie"],
    "kidney beans": ["Beef Chili"],
    "lemon": ["Shrimp Scampi", "Tandoori Chicken"],
    "lettuce": ["Beef Tacos", "Tuna Salad", "Greek Salad"],
    "lime": ["Fish Tacos", "Tacos al Pastor"],
    "ladyfingers": ["Tiramisu"],
    "mascarpone cheese": ["Tiramisu"],
    "milk": ["Pancakes", "French Toast", "Fruit Smoothie", "Omelette"],
    "miso paste": ["Miso Soup"],
    "mozzarella cheese": ["Eggplant Parmesan", "Margarita Pizza"],
    "mushrooms": ["Mushroom Risotto", "Beef and Mushroom Pie"],
    "mustard": ["Beef Wellington"],
    "nori": ["Sushi Rolls", "Ramen"],
    "nuts": ["Baklava"],
    "olive oil": ["Pasta Primavera", "Eggplant Parmesan", "Tomato Basil Soup"],
    "onion": ["Spaghetti Bolognese", "Chicken Curry", "Vegetable Stir Fry", "Pasta Primavera", "Beef Stew", "Tomato Basil Soup", "Beef and Mushroom Pie", "Stuffed Bell Peppers", "Beef Bourguignon", "Pad Thai", "Chicken Shawarma"],
    "parmesan cheese": ["Caesar Salad", "Pasta Primavera", "Eggplant Parmesan", "Mushroom Risotto"],
    "peanuts": ["Pad Thai"],
    "phyllo dough": ["Baklava"],
    "pie crust": ["Quiche Lorraine"],
    "pineapple": ["Tacos al Pastor"],
    "pita bread": ["Chicken Shawarma"],
    "pork": ["Tacos al Pastor"],
    "pork shoulder": ["Pulled Pork Sandwiches"],
    "potato": ["Beef Stew"],
    "rice": ["Chicken Curry", "Chicken Enchiladas", "Mushroom Risotto", "Paella", "Beef Pho"]}

calories_dataset = {
    "arborio rice": 200,
    "avocado": 320,
    "bacon": 43,
    "basil": 2,
    "beans": 130,
    "beef": 250,
    "beef broth": 15,
    "beef fillet": 300,
    "bell pepper": 30,
    "bread": 75,
    "broccoli": 50,
    "brown sugar": 15,
    "butter": 102,
    "cabbage": 25,
    "caesar dressing": 78,
    "carrot": 41,
    "celery": 6,
    "cheddar cheese": 113,
    "cheese": 113,
    "chicken": 190,
    "chicken broth": 5,
    "chili powder": 6,
    "chives": 1,
    "chocolate chips": 70,
    "cilantro": 1,
    "cinnamon": 6,
    "coleslaw": 50,
    "corn": 177,
    "cornstarch": 30,
    "cream": 52,
    "croutons": 122,
    "cucumber": 16,
    "dashi": 10,
    "egg": 70,
    "egg noodles": 210,
    "eggplant": 25,
    "eggs": 70,
    "feta cheese": 75,
    "fettuccine": 210,
    "fish": 170,
    "fish fillet": 200,
    "flour": 455,
    "garlic": 4,
    "ginger": 80,
    "graham cracker crust": 180,
    "green onions": 5,
    "ground beef": 250,
    "heavy cream": 52,
    "honey": 64,
    "key lime juice": 8,
    "kidney beans": 127,
    "lemon": 17,
    "lettuce": 5,
    "lime": 20,
    "ladyfingers": 40,
    "mascarpone cheese": 450,
    "milk": 42,
    "miso paste": 28,
    "mozzarella cheese": 85,
    "mushrooms": 15,
    "mustard": 5,
    "nori": 35,
    "nuts": 165,
    "olive oil": 120,
    "onion": 44,
    "parmesan cheese": 110,
    "peanuts": 166,
    "phyllo dough": 160,
    "pie crust": 330,
    "pineapple": 50,
    "pita bread": 165,
    "pork": 210,
    "pork shoulder": 212,
    "potato": 161,
    "rice": 206,
    "maple syrup": 52,
}

price_dataset = {
    "arborio rice": 3,
    "avocado": 2.5,
    "bacon": 5,
    "basil": 1,
    "beans": 2,
    "beef": 8,
    "beef broth": 1,
    "beef fillet": 10,
    "bell pepper": 1,
    "bread": 2,
    "broccoli": 2,
    "brown sugar": 1,
    "butter": 2,
    "cabbage": 1,
    "caesar dressing": 3,
    "carrot": 1,
    "celery": 0.5,
    "cheddar cheese": 3,
    "cheese": 3,
    "chicken": 6,
    "chicken broth": 1,
    "chili powder": 1,
    "chives": 0.5,
    "chocolate chips": 2,
    "cilantro": 0.5,
    "cinnamon": 1,
    "coleslaw": 2,
    "corn": 2.5,
    "cornstarch": 1.5,
    "cream": 2,
    "croutons": 2.5,
    "cucumber": 1,
    "dashi": 1,
    "egg": 1,
    "egg noodles": 2.5,
    "eggplant": 1,
    "eggs": 1,
    "feta cheese": 2.5,
    "fettuccine": 2.5,
    "fish": 6,
    "fish fillet": 7,
    "flour": 1.5,
    "garlic": 0.5,
    "ginger": 3,
    "graham cracker crust": 4,
    "green onions": 1,
    "ground beef": 8,
    "heavy cream": 2,
    "honey": 3,
    "key lime juice": 1.5,
    "kidney beans": 2,
    "lemon": 1,
    "lettuce": 1,
    "lime": 1,
    "ladyfingers": 2,
    "mascarpone cheese": 8,
    "milk": 2,
    "miso paste": 3,
    "mozzarella cheese": 3,
    "mushrooms": 1,
    "mustard": 1,
    "nori": 2,
    "nuts": 4,
    "olive oil": 5,
    "onion": 1,
    "parmesan cheese": 3,
    "peanuts": 4,
    "phyllo dough": 3.5,
    "pie crust": 6,
    "pineapple": 1.5,
    "pita bread": 3.5,
    "pork": 7,
    "pork shoulder": 7.5,
    "potato": 2.5,
    "rice": 3,
    "maple syrup": 5,
}

recipe_ingredients_dataset = {
    "Banana Bread": ["banana", "baking soda", "butter", "egg", "flour", "sugar"],
    "Beef and Broccoli": ["beef", "broccoli", "brown sugar", "cornstarch", "garlic", "sesame oil", "soy sauce"],
    "Beef Bourguignon": ["bacon", "beef", "beef broth", "carrot", "garlic", "mushrooms", "onion", "red wine"],
    "Beef Chili": ["chili powder", "cumin", "garlic", "ground beef", "kidney beans", "onion", "tomato"],
    "Beef Pho": ["beef", "beef broth", "ginger", "herbs", "onion", "rice noodles", "spices"],
    "Beef Stew": ["beef", "beef broth", "carrot", "celery", "flour", "onion", "potato", "tomato paste"],
    "Beef Tacos": ["avocado", "cheddar cheese", "ground beef", "lettuce", "salsa", "tortillas", "tomato"],
    "Beef Wellington": ["beef fillet", "egg", "mushrooms", "mustard", "puff pastry"],
    "Beef Bulgogi": ["beef", "brown sugar", "garlic", "ginger", "green onions", "sesame oil", "soy sauce"],
    "Baklava": ["butter", "honey", "nuts", "phyllo dough", "spices", "sugar"],
    "Caesar Salad": ["caesar dressing", "croutons", "parmesan cheese", "romaine lettuce"],
    "Chicken Alfredo": ["butter", "chicken", "fettuccine", "garlic", "heavy cream", "parmesan cheese"],
    "Chicken Curry": ["chicken", "coconut milk", "curry powder", "garlic", "ginger", "onion", "rice", "tomato"],
    "Chicken Enchiladas": ["cheddar cheese", "chicken", "enchilada sauce", "onion", "sour cream", "tortillas"],
    "Chicken Noodle Soup": ["carrot", "celery", "chicken", "chicken broth", "egg noodles", "garlic", "onion"],
    "Chicken Shawarma": ["chicken", "garlic", "lemon", "pita bread", "spices", "tahini sauce", "yogurt"],
    "Chocolate Chip Cookies": ["brown sugar", "butter", "chocolate chips", "egg", "flour", "sugar", "vanilla extract"],
    "Creme Brulee": ["egg yolk", "heavy cream", "sugar", "vanilla extract"],
    "Eggplant Parmesan": ["bread crumbs", "eggplant", "mozzarella cheese", "olive oil", "parmesan cheese", "tomato sauce"],
    "Fish Tacos": ["avocado", "cabbage", "cilantro", "fish fillet", "lime", "sour cream", "tortillas"],
    "French Toast": ["bread", "butter", "cinnamon", "egg", "maple syrup", "milk"],
    "Fettuccine Alfredo": ["butter", "fettuccine", "garlic", "heavy cream", "parmesan cheese"],
    "Fruit Smoothie": ["banana", "honey", "milk", "strawberry", "yogurt"],
    "Grilled Cheese Sandwich": ["bread", "butter", "cheese"],
    "Greek Salad": ["cucumber", "feta cheese", "lemon juice", "lettuce", "olive oil", "red onion", "tomato"],
    "Gyoza": ["cabbage", "garlic", "ginger", "green onions", "ground pork", "soy sauce"],
    "Key Lime Pie": ["egg yolks", "graham cracker crust", "key lime juice", "sweetened condensed milk", "whipped cream"],
    "Lentil Soup": ["carrot", "celery", "cumin", "garlic", "lentils", "onion", "tomato", "vegetable broth"],
    "Lobster Bisque": ["butter", "flour", "heavy cream", "lobster", "lobster stock", "sherry"],
    "Margarita Pizza": ["basil", "mozzarella cheese", "olive oil", "pizza dough", "tomato sauce"],
    "Miso Soup": ["dashi", "green onions", "miso paste", "seaweed", "tofu"],
    "Mushroom Risotto": ["arborio rice", "butter", "garlic", "mushrooms", "onion", "parmesan cheese", "white wine"],
    "Pad Thai": ["bean sprouts", "egg", "fish sauce", "peanuts", "rice noodles", "shrimp", "tamarind", "tofu"],
    "Pancakes": ["baking powder", "butter", "egg", "flour", "maple syrup", "milk", "sugar"],
    "Paella": ["bell pepper", "chicken", "chorizo", "onion", "rice", "saffron", "shrimp", "tomato"],
    "Pasta Primavera": ["bell pepper", "garlic", "olive oil", "onion", "pasta", "parmesan cheese", "tomato", "zucchini"],
    "Pulled Pork Sandwiches": ["bbq sauce", "coleslaw", "hamburger buns", "pork shoulder"],
    "Quiche Lorraine": ["bacon", "cheese", "cream", "eggs", "onion", "pie crust"],
    "Ramen": ["bamboo shoots", "broth", "chashu pork", "egg", "green onions", "nori", "ramen noodles"],
    "Ratatouille": ["bell pepper", "eggplant", "garlic", "herbs de Provence", "onion", "tomato", "zucchini"],
    "Shrimp Scampi": ["butter", "garlic", "lemon", "linguine", "parsley", "shrimp", "white wine"],
    "Spinach and Feta Stuffed Chicken": ["chicken breast", "feta cheese", "garlic", "olive oil", "spinach"],
    "Stuffed Bell Peppers": ["bell pepper", "cheese", "ground beef", "onion", "rice", "tomato sauce"],
    "Sushi Rolls": ["fish", "ginger", "nori", "soy sauce", "sushi rice", "vegetables", "wasabi"],
    "Tacos al Pastor": ["cilantro", "lime", "onion", "pineapple", "pork", "tortillas"],
    "Tandoori Chicken": ["chicken", "garlic", "ginger", "lemon", "spices", "yogurt"],
    "Tiramisu": ["cocoa powder", "coffee", "eggs", "ladyfingers", "mascarpone cheese", "sugar"],
    "Tomato Basil Soup": ["basil", "cream", "garlic", "olive oil", "onion", "tomato", "tomato paste", "vegetable broth"],
    "Tuna Salad": ["bread", "canned tuna", "celery", "lettuce", "mayonnaise", "onion", "pickle"],
    "Vegetable Stir Fry": ["bell pepper", "broccoli", "carrot", "garlic", "onion", "sesame oil", "soy sauce"],
    "Vegetarian Chili": ["beans", "bell pepper", "chili powder", "corn", "cumin", "onion", "tomato"]
}

recipe_calories_dataset = {
    "Banana Bread": 350,
    "Beef and Broccoli": 450,
    "Beef Bourguignon": 700,
    "Beef Chili": 500,
    "Beef Pho": 600,
    "Beef Stew": 550,
    "Beef Tacos": 550,
    "Beef Wellington": 800,
    "Beef Bulgogi": 600,
    "Baklava": 350,
    "Caesar Salad": 350,
    "Chicken Alfredo": 800,
    "Chicken Curry": 700,
    "Chicken Enchiladas": 600,
    "Chicken Noodle Soup": 350,
    "Chicken Shawarma": 450,
    "Chocolate Chip Cookies": 150,
    "Creme Brulee": 400,
    "Eggplant Parmesan": 450,
    "Fish Tacos": 400,
    "French Toast": 300,
    "Fettuccine Alfredo": 750,
    "Fruit Smoothie": 200,
    "Grilled Cheese Sandwich": 400,
    "Greek Salad": 300,
    "Gyoza": 400,
    "Key Lime Pie": 350,
    "Lentil Soup": 300,
    "Lobster Bisque": 600,
    "Margarita Pizza": 600,
    "Miso Soup": 150,
    "Mushroom Risotto": 500,
    "Pad Thai": 500,
    "Pancakes": 250,
    "Paella": 700,
    "Pasta Primavera": 450,
    "Pulled Pork Sandwiches": 500,
    "Quiche Lorraine": 450,
    "Ramen": 400,
    "Ratatouille": 250,
    "Shrimp Scampi": 500,
    "Spinach and Feta Stuffed Chicken": 350,
    "Stuffed Bell Peppers": 400,
    "Sushi Rolls": 400,
    "Tacos al Pastor": 400,
    "Tandoori Chicken": 450,
    "Tiramisu": 500,
    "Tomato Basil Soup": 250,
    "Tuna Salad": 350,
    "Vegetable Stir Fry": 300,
    "Vegetarian Chili": 400
}


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
    
    if max_fridge < 100:
      print("Find item from grocery store ")

    max_fridge = user_fridge.max_cal_item()

    if max_fridge in ingredients_recipe_dataset: 
        value = ingredients_recipe_dataset[max_fridge]
    return value 

def mostcom(reference, tocheck):

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
    all_ingredients = []
    for i in recipes:
        if i in recipe_ingredients_dataset:  
            all_ingredients.append(recipe_ingredients_dataset[i])
    return all_ingredients




def stringmatch(commonlists, recipies):
    matching_keys = []
  
    for recipe in recipies:
        if recipe in recipe_ingredients_dataset:
            recipe_ingredients = recipe_ingredients_dataset[recipe]
            for commonlist in commonlists:
                if set(recipe_ingredients).issubset(set(commonlist)):
                    matching_keys.append(recipe)
                    break  # Exit the loop if a match is found for this recipe
    
    return matching_keys


def beststringmatch(commonlists, recipes):
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
    
    tupleitems = fridge.get_items_key()

    totalprice = []
    totalcal = []

    for i in recipe:
        condition = True

        missing_values = []

        x =  recipe_ingredients_dataset[i]
        for y in x:    
            if y not in tupleitems: 
                condition = False
                missing_values.append(y)

        if condition is True: 
            print(f"You have all the items for {i}")
        else: 
            semi_price = 0
            semi_cal = 0
            for item in missing_values: 

                semi_price +=price_dataset[item]
                semi_cal += calories_dataset[item]
            totalprice.append(semi_price)
            totalcal.append(semi_cal)

    efficientlist = [] 
    for i in range(len(recipe)):
        totalpriceitem= totalprice[i] 
        totalcalitem = totalcal[i]
        efficient = totalcalitem/totalpriceitem
        efficientlist.append(efficient)

    maxeff = max(efficientlist)
    maxeff_index = efficientlist.index(maxeff)

    z=  recipe[maxeff_index]
    missing_val = []
    xx = recipe_ingredients_dataset[z]
    for finaltest in xx:    
            if finaltest not in tupleitems: 
                missing_val.append(finaltest)
    

    print(f"You should cook {recipe[maxeff_index]}. However, you are missing {missing_val}.")
 
def main(): 
  
  f = Fridge()

  f.add_item("bread", 500)
  f.add_item("butter", 1)
  f.add_item("cheese", 1)
  f.add_item("onion",1)

  x = find_recipe(f)

  z= recipe_breakdown(x)

  y = f.get_items_key()

  c = mostcom(y,z)

  test = beststringmatch(c , x)

  checkitems(test,f)

main()
    
    