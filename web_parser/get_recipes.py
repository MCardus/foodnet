#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
from lxml import html

# This file get recipes from given links in cookpad.com

def get_recipes(mongodb):
    # Recovering recipes urls from Mongodb
    logging.info("Recovering recipes urls from Mongodb")
    query={}
    filter={"_id":0, "Num_links":0, "Web_parent":0}
    recipes_cursor = mongodb.find(query,filter,collection="recipes_links")
    logging.info("Recipes links recovered. Total recovered links documents: "+str(recipes_cursor.count()))

    # Parsing every bunch of links (every mongo doc. contains many url)
    for recipe_url_list in list(recipes_cursor):
        for recipe_url in recipe_url_list["Web_links"][2:-2].split("', '"):
            logging.debug("Parsing recipe link: "+recipe_url)
            recipe = get_recipe(recipe_url)
            mongodb.save(recipe,"raw_recipes")
            logging.info("Recipe link: "+recipe_url+" parsed and saved")

def get_recipe(recipe_link):
    # Parsing links to obtain recipes
    try:
        recipe = dict()
        ingredients = list()
        title_xpath_selector = "//*[@class='recipe-show__title recipe-title strong field-group--no-container-xs']/text()"
        ingredients_xpath_selector = "//*[@id='ingredients']/div[2]/ol/li"
        page = requests.get(recipe_link)
        tree = html.fromstring(page.content)
        recipe["title"] = tree.xpath(title_xpath_selector)[0].strip()
        logging.info("Recipe with title: "+recipe["title"])
        node_ingredients = tree.xpath(ingredients_xpath_selector)
        for ingredients_line in node_ingredients:
            ingredient = ingredients_line.xpath("normalize-space(.)")
            logging.debug("Recipe contains raw ingredient: "+ingredient)
            ingredients.append(ingredient)
        recipe["ingredients"] = ingredients
        return recipe
    except:
        logging.exception("Recipe link: "+recipe_link+" could not be parsed")
        return None
             
