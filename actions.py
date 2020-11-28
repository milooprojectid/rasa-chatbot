from typing import Any, Text, Dict, List, Union
import re

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted

from app.resources.chatbot_validator import ChatbotValidator
from app.resources.chatbot_helper import ChatbotHelper

chatbot_validator = ChatbotValidator()
chatbot_helper = ChatbotHelper()

class RegistForm(FormAction):

    def name(self):
        return "regist_form"

    @staticmethod
    def required_slots(tracker):
        return [
            'event_conf',
            'nama',
            'email',
            'no_telfon'
            ]

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        ask_event_conf = domain["responses"]["utter_ask_event_conf"][0]["text"]
        ask_nama = domain["responses"]["utter_ask_nama"][0]["text"]
        ask_email = domain["responses"]["utter_ask_email"][0]["text"]
        ask_telfon = domain["responses"]["utter_ask_no_telfon"][0]["text"]

        idx = chatbot_helper.get_event_index(tracker.events)

        tracker_event, tracker_text, latest_message = tracker.events[idx]['event'], tracker.events[idx]['text'], tracker.latest_message['text']

        print(latest_message)
        if latest_message == '/cancel':
            return [
                    SlotSet('event_conf', 'no'),
                    SlotSet('nama', 'no'),
                    SlotSet('email', 'no'),
                    SlotSet('no_telfon', 'no')
                ]

        if tracker_event == 'bot':
            if tracker_text == ask_event_conf:
                if tracker.latest_message['intent']['name'] == 'affirm':
                    return [SlotSet('event_conf', 'yes')]
                return [
                    SlotSet('event_conf', 'no'),
                    SlotSet('nama', 'no'),
                    SlotSet('email', 'no'),
                    SlotSet('no_telfon', 'no')
                ]

            if tracker_text == ask_nama:
                dispatcher.utter_message('Hai {}'.format(latest_message))
                return [SlotSet('nama', latest_message)]

            if tracker_text == ask_email:
                email = chatbot_validator.email_validation(latest_message)
                if email:
                    return [SlotSet('email', email)]
                dispatcher.utter_message('Email yang kamu masukan tidak valid')

            if tracker_text == ask_telfon:
                return [SlotSet('no_telfon', latest_message)]

        return []

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],) -> List[Dict]:
        
        dispatcher.utter_message("Terima kasih {}, data kamu sudah berhasil disimpan".format(tracker.slots["nama"]))
        dispatcher.utter_message("Berikut merupakan data yang kamu masukan\nNama: {}\nEmail: {}\nNo.Telfon: {}".format(tracker.slots["nama"], tracker.slots["email"], tracker.slots["no_telfon"]))
        return [
                    SlotSet('event_conf', None),
                    SlotSet('nama', None),
                    SlotSet('email', None),
                    SlotSet('no_telfon', None)
                ]
