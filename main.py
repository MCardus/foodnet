import web_spider.get_links as web_spider
import utils.init_instances as utils
import utils.db as db_initiator
import ConfigParser

# Loading app config
config_parser = ConfigParser.RawConfigParser()
config_path = 'conf/defaults.cfg'
config_parser.read(config_path)

# Loading mongodb connection instance
utils = utils.Init_instances(config_parser)
mongodb = db_initiator.Db(config_parser, utils)

# Web spider. Generating target links.
mongodb.save("{HELLO WORD : 'MIAU'}","test_collection")
#web_spider.get_links(mongodb)
