n = int(input("n: "))
M = [[int(input("{0},{1}: ".format(i, j))) for j in range(n)] for i in range(n)]

for i in range(0,n,2):
    M[i].sort()

for row in M:
    print(row)
