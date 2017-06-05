
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
            self.logger.exception('Error at saving data: '+body+" into collection: "+collection)
            return str(e)
