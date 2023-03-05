a = int(input("Введите число А: "))
b = int(input("Введите числов В: "))

def degr(a, b):
    if b == 0:
        return 1
    return a*degr(a, b-1)

print(f"A = {a}; B = {b} -> {degr(a, b)}")