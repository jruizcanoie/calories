# Smart Bites
Smart bites aims to help students find easy yet nutritious meals. 

This application is the minimum viable product of Smart Bites and as such does not include all the features that would be expected in the final version of the app. 

# Table of Contents

1. Introduction 
2. Instalation and ussage 
3. Further installments 
4. Credits 


## Introduction 

We created this application for our final project in Algoritihms and Data Strucutes. We were tasked to create an application using techniques which we used in class and create an MVP to present to our class. 

Our MVP of Smart Bites creates, given a set of items inside of the fridge (inputed by the user), a recipie. If items are missing, it will find the most affordable, yet calorie dense meal the student can cook. This way, we are able to keep costs down for the student, whilst still making sure they are getting a good meal. 


**User Journey**: 

Since this is an MVP, the program is run locally on the user's computer. When run, inside the console the user will be asked questions about what they have in their fridge. From there, they will enter the relevant information (one item at a time). 

Once done, our algorithim will give the user the best recepie to cook. 


### File Architecture 

TBD 

### The Datasets 

Our algorithim uses hash tables for faster usage. They are all created by us and are found in _ds.py_. The following is an explanation of what the datasets contain: 
- load_recipe_recipe_database(): Here is the primary dataset where the others stem from. It includes as the key the recipie and as the values both the ingredients needed to cook it, algonside the estimated calories.
- load_recipe_ingredients_recipe_dataset(): This contains as a key the ingredients and as the value the recipie you can make with it. 
- load_recipe_calories_dataset(): In this data set the key is the ingredient and the value is the estimated calories of the item. 
- load_recipe_price_dataset(): In this dataset, we have the ingredient as the key and as the price as the value. 
- load_recipe_recipe_calories_dataset(): Here we have the recipe as the key, and the estimated total calories of the recipe as the value. 
- load_recipe_recipe_ingredients_dataset(): In this dataset, we have the recipe as the key and the ingredients to cook it as the value. 


## Setup

To install this project in edit mode: `pip install -e .`


### Requirements

* Python 3.10+

### Installation

Install it directly into an activated virtual environment:

```text
$ pip install calories
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add calories
```

## Usage

After installation, the package can be imported:

```text
$ python
>>> import calories
>>> calories.__version__
```
