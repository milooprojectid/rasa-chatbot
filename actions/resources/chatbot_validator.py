import re

class ChatbotValidator(object):

    not_valid_general: str = 'Jawaban yang kamu masukan salah'
    not_valid_email: str = 'Email yang kamu masukan tidak valid'

    def email_validation(self, text: str):
        regex_validator = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        for word in text.split():
            if re.match(regex_validator, word):
                return word
        return 

    def phone_number_validation(self, text: str):
        return