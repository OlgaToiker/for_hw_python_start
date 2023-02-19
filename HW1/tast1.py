number = int(input("Введите трехзначное число: "))
if number // 1000 == 0 and number > 100:
    n1 = number//100
    n2 = number//10%10
    n3 = number % 10
    print(f"{number} -> {n1+n2+n3} ({n1}+{n2}+{n3})")
else:
    print(f"Число {number} - не трехзначное.")