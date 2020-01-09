n = int(input("Рядків: "))
m = int(input("Стовпців: "))
a = [[int(input("{0},{1}: ".format(i,j))) for j in range(m)] for i in range(n)]
S = 0
for i in range(n):
   for j in range(m):
        if i != 0 and i % 2 == 0 and j % 2 == 1:
            S += a[i][j]
print(S)
print(a)
