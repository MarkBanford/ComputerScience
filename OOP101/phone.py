from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to parent for attributes
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than 0"

        # Assign to self object
        self.broken_phones = broken_phones
