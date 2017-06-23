from datetime import datetime

class Transaction:
    def __init__(self, slots):
        self.paymentType = "CREDIT" #TODO: Get actual payment type
        self.purchaseDate = datetime.strptime(slots["date"]["value"], "%Y-%m-%d")
        self.business = slots["business"]["value"]
        self.amount = float(slots["dollars"]["value"] + "." + slots["cents"]["value"])
        self.categoryId = 1 #TODO: Get actual category
        self.description = None

    def to_dict(self):
        return {
            "paymentType": self.paymentType,
            "purchaseDate": self.purchaseDate.strftime("%m/%d/%Y %H:%M:%S"),
            "business": self.business,
            "amount": self.amount,
            "categoryId": self.categoryId,
            "description": self.description
        }
