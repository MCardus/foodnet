import web_spider.get_links as web_spider
import web_parser.get_recipes as web_parser
import data_cleaner.recipes_clean as data_cleaner
import utils.init_instances as utils
import utils.db as db_initiator
import ConfigParser
import datetime
import logging

# Loading app config
config_parser = ConfigParser.RawConfigParser()
config_path = 'conf/defaults.cfg'
config_parser.read(config_path)

# Loading logger
date = datetime.datetime.now()
formated_date = "%s_%s_%s" % (date.day, date.month, date.year)
logging.basicConfig(filename='logs/get_links_'+formated_date+'.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=config_parser.get('logging','level'))


# Loading mongodb connection instance
utils = utils.Init_instances(config_parser)
mongodb = db_initiator.Db(config_parser, utils)

# Web spider. Generating target links.
#web_spider.get_links(mongodb)

# Web Parser. Parsing each recipe link
web_parser.get_recipes(mongodb)

# Data cleaner. Clean data to extract ingredients from raw recipes
#data_cleaner.recipes_clean(mongodb)
