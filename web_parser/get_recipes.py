# This file get recipes from given links in cookpad.com

def get_recipes(mongodb):
    print type(mongodb.find(None,"food_corpus"))