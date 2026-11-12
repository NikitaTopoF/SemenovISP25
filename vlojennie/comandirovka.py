n = int(input("Введите сумму количеств цифр N: "))
total = 0
m = 0
while total < n:
    m = m + 1
    total = total + len(str(m))
print(m)