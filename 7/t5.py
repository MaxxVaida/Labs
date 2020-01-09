n = int(input("n: "))
m = int(input("m: "))

A = [
    [int(input("A {0},{1}: ".format(i, j))) for j in range(m)] for i in range(n)
]

count = 0

for col in range(m):
    has_zero = False
    for row in range(n):
        if A[row][col] == 0:
            has_zero = True
            break
    if not has_zero:
        count += 1

print(count)