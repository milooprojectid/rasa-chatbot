import datetime
from actions.resources.db_helper import DBHelper

db_helper = DBHelper()

class Event():

    collection: str = 'events'

    def create(self, data: dict):

        payload = {
            u'user': data['user'],
            u'tanggal': datetime.datetime.now
        }

        return db_helper.post(payload, self.collection)

    def read(self, email: str):
        return db_helper.get(email, self.collection)