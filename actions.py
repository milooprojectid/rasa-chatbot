# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
# from rasa_sdk import Action
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

    # def run(self, dispatcher, tracker, domain):
    #     print(tracker.latest_message)
    #     # tracker.slots["company"] = "Prosa"
    #     print(tracker.slots)
    #     # print(domain)
    #     dispatcher.utter_template("utter_greet", tracker)
    #     # return [SlotSet("nama", "Fahmi"), SlotSet("email", "Fahmi@a.com"), SlotSet("no_telfon", "09890")]
    #     return []

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        
        print("Wawawawa")
        print(tracker.latest_message["text"])
        print(tracker)
        print(dir(tracker))
        print(tracker.slots, tracker.current_state, tracker.latest_action_name)
        # print(tracker.latest_message)
        if "nama" in tracker.latest_message["text"]:
            return [SlotSet("nama", tracker.latest_message["text"])]
        elif "email" in tracker.latest_message["text"]:
            return [SlotSet("email", tracker.latest_message["text"])]
        elif "telfon" in tracker.latest_message["text"]:
            return [SlotSet("no_telfon", tracker.latest_message["text"])]
        # if 
        # slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        # slot_to_fill = tracker.get_slot(REQUESTED_SLOT)

        # if slot_to_fill:
        #     slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))

        # else:
        #     dispatcher.utter_message("Validation failed")

        # return [SlotSet(slot, value) for slot, value in slot_values.items()]
        # return [SlotSet("nama", "Fahmi"), SlotSet("email", "Fahmi@a.com"), SlotSet("no_telfon", "09890")]
        return []

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],) -> List[Dict]:
        
        print("masuk submit")
        dispatcher.utter_message("Terima kasih {}, karena sudah mendaftar".format(tracker.slots["nama"]))
        return []
