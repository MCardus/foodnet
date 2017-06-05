# This file generates all target links. These links will be parsed afterwards.

from lxml import html
import requests
import logging
import datetime


def get_links():
    # Params
    web_parent = "https://cookpad.com/es/buscar/cocina%20tradicional%20espa%C3%B1ola?page="
    host="https://cookpad.com"
    #total_parents = 200
    total_parents = 3
    #xpath_selector="//*[@id='main_contents']/ul"
    xpath_selector=".//ul[@class = 'recipe-list ']/li/a"

    # Parents generation
    list_parents = list()
    #logging.info("Generating parents")
    for parent_id in xrange(1,total_parents):
        #logging.info("Generating parent id:"+str(parent_id))
        actual_parent = "https://cookpad.com/es/buscar/cocina%20tradicional%20espa%C3%B1ola?page="+str(parent_id)
        list_parents.append(actual_parent)

    # Childs generation
    list_childs = list()
    for parent in list_parents:
        page = requests.get(parent)
        tree = html.fromstring(page.content)
        node = tree.xpath(xpath_selector)
        output = "Found "+str(len(node))+" recipe links"
        #logging.info(output)
        tmp_count=0
        for recipe_link in node:
            tmp_count+=1
            current_href=host+recipe_link.get('href')
            list_childs.append(current_href)
            output=str(tmp_count)+","+current_href
            #logging.info(output)


if __name__ == "__main__":
    """
    date = datetime.datetime.now()
    formated_date = "%s_%s_%s" % (date.day, date.month, date.year)
    logging.basicConfig(filename='../logs/get_links_'+formated_date+'.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
    #logging.info("Start get_links")
    """
    get_links()
