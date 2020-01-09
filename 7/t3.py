n = int(input("n: "))
m = int(input("m: "))

A = [
   [int(input("A {0},{1}: ".format(i, j))) for j in range(n)] for i in range(m)
]

x = [int(input("x({0}) = ".format(i))) for i in range(n)]
b = [int(input("b({0}) = ".format(i))) for i in range(n)]

Ax = []

for i in range(m):
   S = 0
   for j in range(n):
       S += A[i][j] * x[j]
   Ax.append(S)

print(Ax)

eq = True
for i in range(n):
   if Ax[i] != b[i]:
       eq = False
       break

print("Ax = b:", eq)
