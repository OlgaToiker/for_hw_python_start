import random

N = int(input("Введите кол-во элементов массива: "))
arr = [random.randint(1, N) for i in range(N)]
print(*arr)
x = int(input("Введите некоторое число Х="))
count = 0
for i in range(0, len(arr)):
    if arr[i] == x:
        count += 1
print(f"-> {count}")