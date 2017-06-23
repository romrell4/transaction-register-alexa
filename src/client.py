import requests

def create_transaction(tx):
    response = requests.post("https://transaction-register.herokuapp.com/transactions", headers = {"Content-Type": "application/json"}, json = tx.to_dict())
    if response.status_code == 200:
        return
    else:
        print(response)
        raise Exception("Error!")