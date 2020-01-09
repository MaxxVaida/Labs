def price(row):
    v = 0
    for el in row:
        if el % 2 == 0 and el > 0:
            v += el
    
    return v

n = int(input("n: "))
m = int(input("m: "))

A = [
    [int(input("A {0},{1}: ".format(i, j))) for j in range(m)] for i in range(n)
]

result = []

prices = list(map(lambda row : price(row), A))
prices.sort()

for p in prices:
    for row in A:
        if price(row) == p:
            result.append(row)
            break

for r in result:
    print(r)
