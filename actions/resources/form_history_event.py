from typing import Any, Text, Dict, List, Union
import re

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

from actions.resources.chatbot_validator import ChatbotValidator
from actions.resources.chatbot_helper import ChatbotHelper, EventHelper
from actions.models import user, event

chatbot_validator = ChatbotValidator()
chatbot_helper = ChatbotHelper()
event_helper = EventHelper()

user = user.User()
event = event.Event()

class HistoryForm(FormAction):

    events: list = []

    def name(self):
        return "history_form"

    @staticmethod
    def required_slots(tracker):
        return [
            'email'
        ]

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        ask_email = domain['responses']['utter_ask_email'][0]['text']

        idx = chatbot_helper.get_event_index(tracker.events)
        tracker_event, tracker_text, latest_message = tracker.events[idx]['event'], tracker.events[idx]['text'], tracker.latest_message['text']

        if latest_message == '/cancel':
            return [SlotSet(row, 0) for row in self.required_slots(tracker)]

        if tracker_event == 'bot':
            if tracker_text == ask_email:
                email = chatbot_validator.email_validation(latest_message)
                if email:
                    res, status_code = user.read(email)
                    if res and status_code == 200:
                        return [SlotSet('email', email)]
                    dispatcher.utter_message(chatbot_validator.email_not_found)
                    return []
                dispatcher.utter_message(chatbot_validator.not_valid_email)
        
        return []

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],) -> List[Dict]:

        if tracker.slots['email'] == 0:
            dispatcher.utter_message('Terima kasih sudah memberikan tanggapan.')

        res, status_code = event.read(tracker.slots['email'])
        if res and status_code == 200:
            for doc in res:
                self.events.append(doc.to_dict())
            dispatcher.utter_message(str(event_helper.get_events(self.events)))
            # dispatcher.utter_message(str(self.events))

        self.events = []
        return [SlotSet(row, None) for row in self.required_slots(tracker)]