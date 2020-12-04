import nltk
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

    def slot_validator(self, text: str) -> list:

        fields = ['nama', 'email', 'telfon', 'pekerjaan']
        result = []

        for word in text.lower().split():
            if re.sub(r'[^a-z]', '', word) in fields:
                result.append(word)
            else:
                for field in fields:
                    distance = nltk.edit_distance(word, field)
                    if distance < len(field) // 2:
                        result.append(field)
        
        if result:
            result.append('data_conf')

        return ['no_telfon' if field == 'telfon' else field for field in result]


if __name__ == "__main__":
    chatbot_validator = ChatbotValidator()
    text = 'nama dan nomor telfon'
    print(chatbot_validator.slot_validator(text))