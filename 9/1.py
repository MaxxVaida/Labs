class Item:
    def __init__(self, name, unit, count):
        self.name = name
        self.unit = unit
        self.count = count
    def __str__(self):
        return "{0} ({1} {2})".format(self.name, self.count, self.unit)

class Storage:
    def __init__(self):
        self.items = []
    
    def deposit(self, item):
        self.items.append(item)

        print("[Storage] + Deposited {0}".format(item))

    def withdraw(self, item_name, count):
        for i in range(len(self.items)):
            it = self.items[i]

            if it.name == item_name:
                it.count -= count
                if it.count < 0:
                    del self.items[i]
                break

        print("[Storage] - Withdrawed {0} by {1}".format(item_name, count))

storage = Storage()

storage.deposit(Item("Potato", "kg", 50))
storage.withdraw("Potato", 25)