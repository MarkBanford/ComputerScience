import csv


# Dealing with Broken phones for example

class Item:
    pay_rate = 0.8
    all = []  # Stored instances
    """ We can use assert to ensure we never receive negative price or quantity"""

    def __init__(self, name: str, price: float, quantity=0):
        # Validations
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)  # add each instance created to the class list

    @property  # getter - ensures you cannot change name after creation
    def name(self):
        return self.__name

    @name.setter  # settr -if we want to set the name
    def name(self, new_name):
        self.__name = new_name

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):  # must be class method as we don't have instances yet i/e Item.insta
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:  # pass in key to retrieve value for instance creation
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))

            )

    @staticmethod
    def is_integer(num):  # remove .0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}Item('{self.name}', {self.price},{self.quantity})"  # Best Practise
