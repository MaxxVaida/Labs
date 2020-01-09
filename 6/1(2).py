import math as ma
n=int(input("Введіть кількість чисел: "))
el=[int(input("Введіть елемент №{0}".format(i+1))) for i in range(n)]
s=1
for i in el:
    s*=i
sg=ma.sqrt(s)
print("Середнє геометричне = {0}".format(sg))
