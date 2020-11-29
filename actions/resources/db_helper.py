import firebase_admin
from firebase_admin import credentials,firestore


cred = credentials.Certificate('./configs/firebase-service-account.json')
firebase_admin.initialize_app(cred)

class DBHelper():

    def __init__(self):
        self.db = firestore.client()

    def post(self, data: dict):
        try:
            doc_ref = self.db.collection(u'users').document(u'harusnya-disini-pake-id-chatbot')
            doc_ref.set({
                u'name': data['nama'],
                u'email': data['email'],
                u'phone': data['no_telfon']
            })
            return {'message': 'success'}, 200
        except Exception as e:
            return {'message': e}, 400
    
    def get(self, email: str):
        try:
            doc_ref = self.db.collection(u'users')
            docs = doc_ref.where('email', '==', email).get()
            return docs, 200
        except Exception as e:
            return e