# Smart Bites
Smart bites aims to help students find easy yet nutritious meals. 

This application is the minimum viable product of Smart Bites and as such does not include all the features that would be expected in the final version of the app. 

# Table of Contents

1. Introduction 
2. Installation and usage 
3. Further installments 
4. Credits 


## Introduction 

We created this application for our final project in Algorithms and Data Structures. We were tasked to create an application using techniques which we used in class and create an MVP to present to our class. 

Our MVP of Smart Bites creates, given a set of items inside of the fridge (imputed by the user), a recipe. If items are missing, it will find the most affordable, yet calorie dense meal the student can cook. This way, we are able to keep costs down for the student, whilst still making sure they are getting a good meal. 


**User Journey**: 

Since this is an MVP, the program is run locally on the user's computer. When run, inside the console the user will be asked questions about what they have in their fridge. From there, they will enter the relevant information (one item at a time). 

Once done, our algorithm will give the user the best recipe to cook. 


### File Architecture 

The most important files are the ones found in `calories`. They include: 

`__init__.py`: Here we are able to import the commands used in `algo.py`. 

`algo.py`: In this file is the MVP of our project. 

`ds.py`: Here are our datasets
### The Datasets 

Our algorithm uses hash tables for faster usage. They are all created by us and are found in _ds.py_. The following is an explanation of what the datasets contain: 
- load_recipe_recipe_database(): Here is the primary dataset where the others stem from. It includes as the key the recipe and as the values both the ingredients needed to cook it, alongside the estimated calories.
- load_recipe_ingredients_recipe_dataset(): This contains as a key the ingredients and as the value the recipe you can make with it. 
- load_recipe_calories_dataset(): In this data set the key is the ingredient and the value is the estimated calories of the item. 
- load_recipe_price_dataset(): In this dataset, we have the ingredient as the key and as the price as the value. 
- load_recipe_recipe_calories_dataset(): Here we have the recipe as the key, and the estimated total calories of the recipe as the value. 
- load_recipe_recipe_ingredients_dataset(): In this dataset, we have the recipe as the key and the ingredients to cook it as the value. 


## Setup
You will need a valid python installation in your machine to run this project in development form.  After checking out the project through the usual `git checkout https://github.com/jruizcanoie/calories.git` and creating a virtual environment to isolate this project from your main python installation (recommended, but not necessary), do simply execute `pip install -e .` to install this project in edit mode.

When the project is install either in edit mode or through a conventional `pip install` command (see Build section below), a command line script called `calories` will be able at terminal to execute the program.

### Requirements

* Python 3.8.5+

### How to build 

Simply run `poetry build` and the wheels will be located in the `dist` directory.  The file with extension `whl` is a wheel installation file that you could use to setup a different virtual environment by running `pip install calories-1.0-py3-none-any.whl`.


## Usage

After installation, simply write `calories` in the command line and the program will run. 

IMPORTANT: Some ingredients may not exist in the datasets and therefore the program will not be able to run. 
We recommend to try first the following ingredients to make sure the program is installed correctly: Bread, butter. The program should return Grilled cheese as a recipe. 

Note: Since we want the recipes to be nutritious, at least one of the ingredients added by the user must be over 100 calories.  Otherwise the program will return to buy ingredients at the store. We made it this way to make sure the recipe had some sort of nutritious base (such as pasta, meat etc..). 


## Credits: 

* Justo Ruiz Cano 
* Javier Alonso 
* Nicolas Loescher Montal 
* Paul Coyral 