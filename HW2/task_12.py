sum = int (input("Введите сумму загаданных чисел x и y: "))
comp = int(input("Введите произведение загаданных чисел x и y: "))
def numbers(s, c):
    for i in range(s):
        for j in range(c):
            if s == i + j and c == i * j:
                return f"{i}  {j}"
    return "Решения нет, т.к. такой комбинации чисел не существует."
print(numbers(sum, comp))