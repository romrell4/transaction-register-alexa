from service_exception import ServiceException
from transaction import Transaction
import client

def handler(event, context):
    print(event)

    # Get the intent info
    intent = event["request"]["intent"]
    intent_name = intent["name"]

    # Get the current state
    session = event["session"]
    state = None
    if "state" in session["attributes"]:
        state = session["attributes"]["state"]

    if intent_name == "Start":
        payment_type = intent["slots"]["payment_type"]["value"]
        session["attributes"]["state"] = payment_type
        return format_response(session, "I'm ready whenever you are")
    elif intent_name == "EnterTransaction" and state is not None:
        if "dialogState" in intent and intent["dialogState"] != "COMPLETE":
            return format_response(session, "I don't know how to do this yet... Check my logs")
        else:
            try:
                tx = Transaction(intent["slots"])
                client.create_transaction(tx)
                return format_response(session, "Got it")
            except ServiceException as e:
                return format_response(session, e)
    else:
        return format_response(session, "I didn't understand that. Please try again.")

def format_response(session, text, reprompt_text = "", state = None, finish = False):
    response = {
        "version": "1.0",
        "session": session,
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": text
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": reprompt_text
                }
            },
            "shouldEndSession": finish
        }
    }
    print(response)
    return response

def dialog_delegate():
    # TODO: Fill this out with the correct data (probably needs slots passed in...) https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/dialog-interface-reference#delegate
    response = {
        "type": "Dialog.Delegate",
        "updatedIntent": {
            "name": "",
            "confirmationStatus": "NONE",
            "slots": {
                "PUT_SLOT_HERE": {
                    "name": "",
                    "value": "",
                    "confirmationStatus": "NONE"
                }
            }
        }
    }
    print(response)
    return response
