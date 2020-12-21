from firebase_admin import credentials, firestore
import firebase_admin

import uuid

cred = credentials.Certificate('./configs/firebase-service-account.json')
firebase_admin.initialize_app(cred)

class DBHelper():

    def __init__(self):
        self.db = firestore.client()

    def post(self, payload: dict, collection_name: str):
        try:
            doc_ref = self.db.collection(collection_name).document(str(uuid.uuid4()))
            doc_ref.set(payload)
            return {'message': 'success'}, 200
        except Exception as e:
            return {'message': e}, 400
    
    def get(self, email: str, collection_name: str):
        try:
            doc_ref = self.db.collection(collection_name)
            docs = doc_ref.where('email', '==', email).get()
            return docs, 200
        except Exception as e:
            return {'message': e}, 404

    def put(self, id_: str, payload: dict, collection_name: str):
        try:
            doc_ref = self.db.collection(collection_name).document(id_)
            doc_ref.update(payload)
            return {'message': 'success'}, 200
        except Exception as e:
            return {'message': e}, 400

# import re
# from datetime import datetime

# if __name__ == '__main__':
#     a = []
#     tanggal = '2020-12-08 19:44:34.849431'
#     # tanggal_split = tanggal.split(':')
#     # tanggal_split[-1] = str(round(float(tanggal_split[-1])))

#     datetime_format = '%Y-%m-%d %H:%M:%S.%f'
#     datetime_object = datetime.strptime(tanggal, datetime_format)
#     print(type(datetime_object))
#     print(datetime_object)
#     a.append(datetime_object)
#     # tanggal_final = ':'.join(tanggal_split)


# from datetime import datetime

# datetime_str = '09/19/18 13:55:26'

# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

# print(type(datetime_object))
# print(datetime_object)  # printed in default format

# a.append(datetime_object)

# print(sorted(a, reverse=True)[:1])