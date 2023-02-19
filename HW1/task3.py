number = int(input("Введите билет с шестизначным номером: "))
n1 = number//1000
n2 = number % 1000
if number // 1000000 == 0 and number >= 100000 and n1//100 + n1//10 % 10 + n1 % 10 == n2//100 + n2//10 % 10 + n2 % 10:
    print(f"{number} -> yes")
else:
    print(f"{number} -> no")