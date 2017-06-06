# This file get recipes from given links in cookpad.com

def get_recipes(mongodb): 
    print mongodb.find(collection="food_corpus")
