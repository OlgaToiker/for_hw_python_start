n = int(input("Введите длину n-стороны шоколадки: "))
m = int(input("Введите длину m-стороны шоколадки: "))
k = int(input("Введите k-кусочков: "))
if k < n*m and (k % n == 0 or k % m == 0):
    # в строке выше нужны скобки, иначе при размере 1*4 и 4 кусочках будет выдаваться ответ yes (а это в моем понимании задачи неверно)
    print(f"{n} {m} {k} -> yes")
else:
    print(f"{n} {m} {k} -> no")