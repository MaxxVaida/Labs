a=int(input("Введіть кількість чисел масиву: "))
b=[int(input("Введіть {0} число: ".format(i+1))) for i in range(a)]
b.sort(reverse=True)
print(b)