from firebase_admin import firestore
from actions.resources.db_helper import DBHelper

db_helper = DBHelper()

class User():

    collection: str = 'users'

    def create(self, data: dict):

        payload = {
            u'nama': data['nama'],
            u'email': data['email'],
            u'no_telfon': data['no_telfon'],
            u'pekerjaan': data['pekerjaan']
        }

        return db_helper.post(payload, self.collection)

    def read(self, email: str):
        return db_helper.get(email, self.collection)