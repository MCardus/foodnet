# This file generates all target links. These links will be parsed afterwards.

from lxml import html
import requests

def get_links():
  # Params
  web_parent = "https://cookpad.com/es/buscar/cocina%20tradicional%20espa%C3%B1ola?page="
  #total_parents = 200
  total_parents = 2
  
  # Parents generation
  list_parents = list()
  for parent_id in xrange(total_parents):
    actual_parent = "https://cookpad.com/es/buscar/cocina%20tradicional%20espa%C3%B1ola?page="+parent_i
    list_parents.append(actual_parent)
  
  # Childs generation
  list_childs = list()
  for parent in list_parents:
    page = requests.get(parent)
    tree = html.fromstring(page.content)

if __name__ == "__main__":
  get_links()
