n=int(input("Введіть кількість осей: "))
v=[int(input("Введіть {0} координату: ".format(i+1))) for i in range(n)]
k=int(input("Введіть друге число: "))
res=[i*k for i in v]
print("{0}*{1}={2}".format(v,k,res))
