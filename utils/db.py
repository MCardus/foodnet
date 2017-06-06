import logging
import datetime

class Db(object):
    """
    This class provides low level DB acces.
    """
    def __init__(self, config, utils):
        self.db = utils.get_db()
        self.config = config
        #date = datetime.datetime.now()
        #formated_date = "%s_%s_%s" % (date.day, date.month, date.year)
	#logging.setLevel(logging.EXCEPTION)
        #Logger.basicConfig(filename='logs/get_links_'+formated_date+'.log',
        #                        filemode='a',
        #                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        #                        datefmt='%H:%M:%S',
        #                        level=logging.DEBUG)


    def save(self, body, collection):
        try:
            self.db[collection].insert(body)
        except Exception as e:
            logging.exception('Error at saving data: '+body+" into collection: "+collection)
            return str(e)

    def find(self,query=None,collection=None):
        try:
            self.db[collection].find(query)
        except Exception as e:
            logging.exception('Error at reading data using query: ' + query + " into collection: " + collection)
            return str(e)

