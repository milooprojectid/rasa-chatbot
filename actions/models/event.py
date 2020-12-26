import datetime
from actions.resources.db_helper import DBHelper

db_helper = DBHelper()

class Event():

    collection: str = 'events'

    def create(self, data: dict):

        payload = {
            u'user': data,
            u'email': data['email'],
            u'tanggal': datetime.datetime.now().__str__(),
            u'detail': {
                'nama': 'Judul event',
                'jenis': 'Ngemil',
                'kategori': 'Hacker'
            }
        }

        return db_helper.post(payload, self.collection)

    def read(self, email: str):
        return db_helper.get(email, self.collection)