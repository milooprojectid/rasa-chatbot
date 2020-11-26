import re

class ChatbotHelper(object):

    def __init__(self):
        pass

    def email_validation(self, text: str):
        regex_validator = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        for word in text.split():
            if re.match(regex_validator, word):
                return word
        return 