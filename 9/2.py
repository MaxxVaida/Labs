class Product:
    def __init__(self, name, unit, count, cost):
        self.name = name
        self.unit = unit
        self.count = count
        self.cost = cost
    def __str__(self):
        return "{0} ({1} {2}, {3} per {2})".format(self.name, self.count, self.unit, self.cost)

class Storage:
    def __init__(self):
        self.products = []

    def add_product(self, p):
        self.products.append(p)

    def get_all_products(self):
        return self.products

    def searcher(self, item, criteria, query):
        if criteria == "name":
            return query in item.name
        elif criteria == "count":
            return float(query) <= item.count
        elif criteria == "cost":
            return abs(float(query) - item.cost) < 0.0001
        else:
            return False

    def search(self, criteria, query):
       return [item for item in self.products if self.searcher(item, criteria, query)]

############################

storage = Storage()

n = int(input("How many products? "))
for i in range(n):
    name = input("Product #{0}, Name = ".format(i+1))
    unit = input("Product #{0}, Unit = ".format(i+1))
    count = float(input("Product #{0}, Count = ".format(i+1)))
    cost = float(input("Product #{0}, Cost = ".format(i+1)))
    
    storage.add_product(
        Product(name, unit, count, cost)
    )
    
    print("\n")

print("[Storage]")
for p in storage.get_all_products():
    print(p)

print("\n[Search]")
criteria = input("Search criteria (name, count, cost): ")
query = input("Search query: ")
print("RESULTS:")

for p in storage.search(criteria, query):
    print(p)