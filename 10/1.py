import math

class Vector:
    def __init__(self, coords):
        self.coords = coords
        self.size = len(coords)

    def input(self):
        for i in range(self.size):
            coord = float(input("Coord #{0} = ".format(i+1)))
            self.coords[i] = coord
    
    def __str__(self):
        cstr = ""

        for i in range(self.size):
            c = self.coords[i]
            cstr += str(c)

            if i != self.size-1:
                cstr += ', '

        return "Vector{0}D ({1})".format(self.size, cstr)

    def length(self):
        s = 0
        for c in self.coords:
            s += c * c
        return math.sqrt(s)

    def normalize(self):
        l = self.length()

        for i in range(self.size):
            self.coords[i] = self.coords[i] / l

v = Vector([3,4,5,6])
print(v)
v.input()

print("length =",v.length())

v.normalize()
print("normalized =", v)