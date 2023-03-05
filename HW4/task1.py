n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))
s1 = set()
s2 = set()
for i in range(1, n+1):
    i = int(input())
    s1.add(i)
print(s1)
for i in range(1, m+1):
    i = int(input())
    s2.add(i)
print(s2)
unific = list(s1.intersection(s2))
print(sorted(unific))