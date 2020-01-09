import math

def g(i):
    if i == 0:
        return 9
    elif i == 1:
        return 35
    else:
        return math.sin(g(i-1) + math.cos(g(i-2)))


s = g(7) + g(9)
print("s = {0}".format(s))
