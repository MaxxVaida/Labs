class Rectangle:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Rectangle ({0}, {1})".format(self.a, self.b)

    def input(self):
        self.a = float(input("Rectangle Width = "))
        self.b = float(input("Rectangle Height = "))

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2

    def __eq__(self, other):
        return abs(self.area() - other.area()) < 0.0001
    
    def __add__(self, other):
        return Rectangle(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Rectangle(self.a * other.a, self.b - other.b)

    def __mul__(self, n):
        return Rectangle(self.a * n, self.b * n)

test = Rectangle(3,5)
print(test)
print("S = {0}".format(test.area()))
print("P = {0}".format(test.perimeter()))
print("+(7,5) = {0}".format(test + Rectangle(7,5)))
print("*5 = {0}".format(test * 5))
print("eq (3,5) = {0}".format(test == Rectangle(3,5)))
print("eq (6,10) = {0}".format(test == Rectangle(6, 10)))
