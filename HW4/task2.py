import random
n = int(input("Введите кол-во кустов: "))
b = [random.randint(0, 10) for _ in range(n)]
print(b)
b.extend([b[0], b[1]])
sum=0
for i in range (len(b)-2):
    sum3 = b[i]+b[i+1]+b[i+2]
    if sum3 > sum:
        sum = sum3
print(sum)