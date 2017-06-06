import logging
import datetime

class Db(object):
    """
    This class provides low level DB acces.
    """
    def __init__(self, config, utils):
        self.db = utils.get_db()
        self.config = config

    def save(self, body, collection):
        try:
            self.db[collection].insert(body)
        except Exception as e:
            logging.exception('Error at saving data: '+body+" into collection: "+collection)
            return str(e)

    def find(self,query=None,collection=None):
        ret = None
        try:
            ret = self.db[collection].find(query)
        except Exception as e:
            logging.exception('Error at reading data using query: ' + query + " into collection: " + collection)
            ret = str(e)
        return ret

