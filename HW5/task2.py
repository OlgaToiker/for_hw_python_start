a = int(input("Введите целое неотрицательное число a: "))
b = int(input("Введите целое неотрицательное число b: "))

def sum(a, b):
    if b == 0:
        return a
    return sum(a, b - 1) + 1

print(sum(a, b))