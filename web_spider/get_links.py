# This file generates all target links. These links are parsed afterwards.

from lxml import html
import logging
import datetime
import requests

def get_links(mongodb):
    # Params
    web_parent = "https://cookpad.com/es/buscar/cocina%20tradicional%20espa%C3%B1ola?page="
    host="https://cookpad.com"
    total_parents = 200
    xpath_selector=".//ul[@class = 'recipe-list ']/li/a"

    # Parents generation
    list_parents = list()
    logging.debug("Generating parents")
    for parent_id in xrange(1,total_parents):
        logging.debug("Generating parent id:"+str(parent_id))
        actual_parent = "https://cookpad.com/es/buscar/cocina%20tradicional%20espa%C3%B1ola?page="+str(parent_id)
        list_parents.append(actual_parent)

    # Childs generation
    for parent in list_parents:
        try:
            list_childs = list()
            page = requests.get(parent)
            tree = html.fromstring(page.content)
            node = tree.xpath(xpath_selector)
            output = "Found "+str(len(node))+" recipe links from parent "+parent+"\n"
            tmp_count=0
            for recipe_link in node:
                tmp_count+=1
                current_href=host+recipe_link.get('href')
                list_childs.append(current_href)
                output+=str(tmp_count)+","+current_href+"\n"
            logging.debug(output)

            # Writing results in mongodb
            result = dict()
            result['Web_links']=str(list_childs)
            result['Web_parent']=parent
            result['Num_links']=str(len(node))
            mongodb.save(result,"recipes_links")
	except:
	    logging.exception("ERROR with parent: "+parent)


if __name__ == "__main__": 
    get_links()
