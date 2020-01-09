import math


def f(x):
    return math.sqrt(4*x + math.sin(math.sqrt(x**3)))


def integral(a, b, n):
    h = (b - a) / n

    S = 0

    for i in range(0, n):
        S += f(a + h * i)

    S *= h

    return S


a = float(input("a = "))
b = float(input("b = "))
n = int(input("n = "))

result = integral(a, 3, n) + integral(a, b, n)

print(result)
