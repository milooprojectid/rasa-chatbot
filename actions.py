# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List, Union
import re

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted

class RegistForm(FormAction):

    def name(self):
        return "regist_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "nama",
            "email",
            "no_telfon"
            ]

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        ask_nama = domain["responses"]["utter_ask_nama"][0]["text"]
        ask_email = domain["responses"]["utter_ask_email"][0]["text"]
        ask_telfon = domain["responses"]["utter_ask_no_telfon"][0]["text"]

        i = len(tracker.events) - 1
        while i >= 0 and tracker.events[i]["event"] != "bot":
            i -= 1

        if tracker.events[i]["event"] == "bot":
            if tracker.events[i]["text"] == ask_nama:
                dispatcher.utter_message("Hai {}".format(tracker.latest_message["text"]))
                return [SlotSet("nama", tracker.latest_message["text"])]
            if tracker.events[i]["text"] == ask_email:
                regex_validator = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                for word in tracker.latest_message["text"].split():
                    if '@' in tracker.latest_message["text"] and re.search(regex_validator, word):
                        return [SlotSet("email", word)]
                else:
                    dispatcher.utter_message("Email yang kamu masukan tidak valid")
            if tracker.events[i]["text"] == ask_telfon:
                return [SlotSet("no_telfon", tracker.latest_message["text"])]

        return []

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],) -> List[Dict]:
        
        dispatcher.utter_message("Terima kasih {}, data kamu sudah berhasil disimpan".format(tracker.slots["nama"]))
        dispatcher.utter_message("Berikut merupakan data yang kamu masukan\nNama: {}\nEmail: {}\nNo.Telfon: {}".format(tracker.slots["nama"], tracker.slots["email"], tracker.slots["no_telfon"]))
        return []
