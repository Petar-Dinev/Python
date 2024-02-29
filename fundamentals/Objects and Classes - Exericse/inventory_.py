class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return int(self.__capacity)

    def __repr__(self):
        items = ', '.join(self.items)
        left_capacity = self.__capacity
        return f"Items: {items}.\nCapacity left: {left_capacity}"
