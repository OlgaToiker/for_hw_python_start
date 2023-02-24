n = int(input("Введите кол-во монет: "))
count_0 = 0
count_1 = 0
for i in range (n):
    coin = input("Введите 1 (орел) или 0 (решка): ")
    if coin == "1":
        count_1 += 1
    else:
        count_0 += 1
if count_1 >= count_0:
    print(count_0)
else:
    print(count_1)