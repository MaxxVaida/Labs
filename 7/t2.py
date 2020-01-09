def ask_matrix(name, rows, cols):
    return [[int(input("{0} {1},{2}: ".format(name, i, j))) for j in range(cols)] for i in range(rows)]
n = int(input("n: "))
m = int(input("m: "))
A = ask_matrix("A", n, m)
B = ask_matrix("B", n, m)
for i in range(n):
    for j in range(m):
        if A[i][j] == 0:
            A[i][j] = B[i][j]
for row in A:
    print(row)
