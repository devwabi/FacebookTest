# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionYesNo(Action):
    def name(self) -> Text:
        return "action_yes_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if tracker.get_latest_input_channel() == 'facebook':
            message = {
                "text": "Is this correct (Yes/No/YesNo)?",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Yes",
                        "payload": "/affirm",
                    }, {
                        "content_type": "text",
                        "title": "No",
                        "payload": "/deny",
                    },{
                        "content_type": "text",
                        "title": "YesNo",
                        "payload": "/deny",
                    },{
                        "content_type": "text",
                        "title": "NoYes",
                        "payload": "/deny",
                    }
                    
                    
                ]
            }
            dispatcher.utter_custom_json(message)

        else:
            dispatcher.utter_message(template="utter_greet")
        return []





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
