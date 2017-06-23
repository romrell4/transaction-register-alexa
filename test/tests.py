import unittest

from src import main

class MyTest(unittest.TestCase):
    def test_start(self):
        self.set_up_event("Start", state = None, data = {
            "payment_type": "credit"
        })
        self.execute()

    def test_enter_transaction(self):
        self.set_up_event("EnterTransaction", state = "CREDIT", data = {
            "date": "2018-06-22",
            "business": "Fred Meyer",
            "dollars": "20",
            "cents": "05",
            "category": "food"
        })
        self.execute()

    def set_up_event(self, intent, state = None, data = None):
        attributes = {} if state is None else {"state": state}
        slots = {}
        if data is not None:
            for key in data:
                slots[key] = {
                    "name": key,
                    "value": data[key]
                }

        self.event = {
            "session": {
                "attributes": attributes,
            },
            "request": {
                "intent": {
                    "name": intent,
                    "slots": slots
                }
            },
            "version": "1.0"
        }

    def execute(self):
        return main.handler(self.event, None)
