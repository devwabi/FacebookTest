# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import any, text, dict, list
#
from rasa_sdk import action, tracker
from rasa_sdk.executor import collectingdispatcher

class ActionYesNo(Action):
    def name(self):
        return "action_yes_no"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_latest_input_channel() == 'facebook':
            message = {
                "text": "Is this correct (Yes/No)?",
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
                    }
                    
                    
                ]
            }
            dispatcher.utter_custom_json(message)
        
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
