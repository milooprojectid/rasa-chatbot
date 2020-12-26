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
