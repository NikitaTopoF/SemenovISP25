s = int(input("Введите количество дней: "))
p = 10
for i in range(s - 1):
    p += p * (10/100)
print(f"Суммарный путь за s дней:", p)    