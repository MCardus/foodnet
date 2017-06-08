import logging

# Recipes cleaning for extracting ingredients from raw recipes


def recipes_clean(mongodb):
    logging.info("Starting cleaning recipes")
    # Get food coorpus
    food_corpus = load_food_corpus(mongodb)
    # Get raw recipes cursor
    raw_recipes = mongodb.find(filter={"_id":0}, collection="raw_recipes_latin")
    logging.info("Raw recipes recovered from mongodb. Total of: "+str(raw_recipes.count))
    total_cleaned_recipes = 0
    for raw_recipe in list(raw_recipes):
        recipe = dict()
        title = raw_recipe["title"].encode("latin-1")
        try:
            ingredients = parse_ingredients(raw_recipe["ingredients"], food_corpus, mongodb)
            recipe["title"] = title
            recipe["ingredients"] = ingredients
            mongodb.save(recipe, "clean_recipes")
            total_cleaned_recipes += 1
            logging.debug("Recipe "+title+" cleaned. Ingredients list: "+str(ingredients))
        except:
            logging.exception("Error recipe could not be cleaned. Error happend in iteration: "+str(total_cleaned_recipes))
    logging.info("Total of "+str(total_cleaned_recipes)+" recipes have been parsed")
    
def load_food_corpus(mongodb):
    # Retrieving corpus data from mongodb
    logging.info("Recovering food coorpus from mongodb")
    try:
        food_corpus_cursor = list(mongodb.find(filter={"_id": 0}, collection="food_corpus"))
        food_corpus = dict()
        for ingredient in food_corpus_cursor:
            logging.debug("Next corpus ingredient: "+str(ingredient))
            try:
                spanish_name = ingredient["SpanishName"].lower()
                english_name = ingredient["EnglishName"].lower()
            except:
                logging.exception("Current ingredient "+str(ingredient)+" could not be loaded")
            food_corpus[spanish_name] = english_name
        logging.info("Food corpus correctly loaded. Total loaded ingredients: "+str(len(food_corpus))+" Ingredients list:\n"+str(food_corpus))
        return food_corpus
    except:
        logging.exception("Food corpus could not be loaded")
        food_corpus = {}
    return food_corpus

def parse_ingredients(ingredients_raw, food_corpus, mongodb):
    # TODO - Improve function code quality
    ingredients_clean = list()
    for sentence in ingredients_raw:
        clean_ingredient = None
        logging.debug("Trying to parse sentence: "+sentence)
        sentence_split = sentence.lower().split(" ")
        # Check groups of works size = 3
        for count in xrange(len(sentence_split)):
            if clean_ingredient == None:
                try:
                    current_combination = sentence_split[count]+" "+sentence_split[count+1]+" "+sentence_split[count+2]
                    if current_combination in food_corpus:
                        logging.debug("Ingredient found in present sentence: "+current_combination)
                        clean_ingredient = current_combination
                    if clean_ingredient != None:
                       logging.debug("Ingredient cleaned! "+current_combination+" is "+clean_ingredient)
                       ingredients_clean.append(clean_ingredient)

                except:
                    pass
	if clean_ingredient == None:
	    # Check groups of works size = 2
            for count in xrange(len(sentence_split)):
                if clean_ingredient == None:
                    try:
                        current_combination = sentence_split[count]+" "+sentence_split[count+1]
                        if current_combination in food_corpus:
                            logging.debug("Ingredient found in present sentence: "+current_combination)
                            clean_ingredient = current_combination
                        if clean_ingredient != None:
                           logging.debug("Ingredient cleaned! "+current_combination+" is "+clean_ingredient)
                           ingredients_clean.append(clean_ingredient)

                    except:
                        pass
            if clean_ingredient == None:
                # Check groups of works size = 1
                for word in sentence_split:
                   if clean_ingredient == None:
                       if word in food_corpus:
                           logging.debug("Ingredient found in present sentence: "+word)
                           clean_ingredient = word
	               elif word[:-1] in food_corpus:
                           logging.debug("Ingredient found in present sentence: "+word[:-1])
 	                   clean_ingredient = word[:-1]
                       elif word+"s" in food_corpus:
                           logging.debug("Ingredient found in present sentence: "+word+"s")
                           clean_ingredient = word+"s"
                       elif word+"es" in food_corpus:
                           logging.debug("Ingredient found in present sentence: "+word+"es")
	                   clean_ingredient = word+"es"
                       if clean_ingredient != None: 
                           logging.debug("Ingredient cleaned! "+word+" is "+clean_ingredient)
                           ingredients_clean.append(clean_ingredient)
        if clean_ingredient == None:
            logging.debug("Present sentence "+sentence+" could not be parsed")
            try:
                mongodb.save({"sentence":sentence},"ingredients_not_found")
            except:
                pass
    return ingredients_clean
