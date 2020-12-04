from typing import Any, Text, Dict, List, Union
import re

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted

from actions.resources.chatbot_validator import ChatbotValidator
from actions.resources.chatbot_helper import ChatbotHelper
from actions.resources.db_helper import DBHelper
from actions.models.user import User

chatbot_validator = ChatbotValidator()
chatbot_helper = ChatbotHelper()

user = User()

class RegistForm(FormAction):

    already_registered: bool = False
    updated: bool = False

    def name(self):
        return "regist_form"

    @staticmethod
    def required_slots(tracker):
        return [
            'event_conf',
            'email',
            'nama',
            'no_telfon',
            'pekerjaan',
            'data_conf',
            'data_valid'
        ]

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        ask_event_conf = domain['responses']["utter_ask_event_conf"][0]["text"]
        ask_nama = domain['responses']["utter_ask_nama"][0]["text"]
        ask_email = domain['responses']["utter_ask_email"][0]["text"]
        ask_telfon = domain['responses']["utter_ask_no_telfon"][0]["text"]
        ask_pekerjaan = domain['responses']["utter_ask_pekerjaan"][0]["text"]
        ask_data_conf = domain['responses']["utter_ask_data_conf"][0]["text"]
        ask_wrong_data = domain['responses']["utter_ask_data_valid"][0]["text"]

        idx = chatbot_helper.get_event_index(tracker.events)

        tracker_event, tracker_text, latest_message = tracker.events[idx]['event'], tracker.events[idx]['text'], tracker.latest_message['text']

        intent, confidence = tracker.latest_message['intent']['name'], tracker.latest_message['intent']['confidence']

        if latest_message == '/cancel':
            return [SlotSet(row, 0) for row in self.required_slots(tracker)]

        if tracker_event == 'bot':
            if tracker_text == ask_event_conf:
                if confidence > 0.8:
                    if intent == 'affirm':
                        return [SlotSet('event_conf', 'yes')]
                    if intent == 'deny':
                        return [SlotSet(row, 0) for row in self.required_slots(tracker)]
                dispatcher.utter_message(chatbot_validator.not_valid_general)

            if tracker_text == ask_email:
                email = chatbot_validator.email_validation(latest_message)
                if email:
                    res, status_code = user.read(email)
                    if res and status_code == 200:
                        doc = res[0].to_dict()
                        self.already_registered = True
                        return [SlotSet(key, doc[key]) for key in doc]
                    return [SlotSet('email', email)]
                dispatcher.utter_message(chatbot_validator.not_valid_email)

            if tracker_text == ask_nama:
                dispatcher.utter_message('Hai {}'.format(latest_message))
                return [SlotSet('nama', latest_message)]

            if tracker_text == ask_telfon:
                return [SlotSet('no_telfon', latest_message)]

            if tracker_text == ask_pekerjaan:
                return [SlotSet('pekerjaan', latest_message)]

            if '\n' in tracker_text:
                if tracker_text.split('\n')[-1] == ask_data_conf.split('\n')[-1]:
                    if confidence > 0.8:
                        if intent == 'affirm':
                            return [
                                SlotSet('data_conf', 'yes'),
                                SlotSet('data_valid', 'yes')
                            ]
                        if intent == 'deny':
                            self.updated = True
                            return [SlotSet('data_conf', 'no')]
                    dispatcher.utter_message(chatbot_validator.not_valid_general)

            if tracker_text == ask_wrong_data:
                if intent == 'affirm' and confidence > 0.9:
                    return [SlotSet('data_conf', None)]
                slots = chatbot_validator.slot_validator(latest_message)
                if slots:
                    return [SlotSet(slot, None) for slot in slots]

        return []

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],) -> List[Dict]:

        if tracker.slots['event_conf'] == 0:
            dispatcher.utter_message('Terima kasih sudah memberikan tanggapan.')
            return [SlotSet(row, None) for row in self.required_slots(tracker)]

        dispatcher.utter_message('terimakasih')

        # if not self.already_registered:
        #     res, status_code = db_helper.get(tracker.slots['email'])
        #     if not res and status_code == 200:
        #         res, status_code = db_helper.post({
        #             'nama': tracker.slots['nama'],
        #             'email': tracker.slots['email'],
        #             'no_telfon': tracker.slots['no_telfon']
        #         })

        #         if status_code == 200:
        #             dispatcher.utter_message("Terima kasih {}, data kamu sudah berhasil disimpan".format(tracker.slots["nama"]))
                
        #             return []
        
        if self.already_registered:
            dispatcher.utter_message("Terima kasih {}, data kamu sudah berhasil disimpan".format(tracker.slots["nama"]))

            self.already_registered = False
        
            return []

        return [SlotSet(row, None) for row in self.required_slots(tracker)]
