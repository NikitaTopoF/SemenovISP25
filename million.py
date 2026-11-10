n = int(input("Введите число:"))
for i in range(2, n):
    for delitel in range(2, i):
            if i % delitel == 0:
                break
    else: print(i)