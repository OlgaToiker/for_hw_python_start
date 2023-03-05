import random
N = int(input("Введите кол-во элементов массива: "))
arr = [random.randint(1, N) for i in range(N)]
print(*arr)
x = int(input('Заданное число: '))
j = 0
i = 0
min_diff = abs(x - arr[i])
for i in range(N):
    if abs(x-arr[i]) <= min_diff:
        min_diff = abs(x-arr[i])
        j = i
        i += 1
print(f"Самый близкий по величине элемент -> {arr[j]}")