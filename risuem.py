h = int(input("Высота: "))
b = int(input("Ширина: "))
s = str(input("Символ: "))
for i in range(h):
    if i == 0 or i == h - 1:
        print(s * b)
    else:
        print(s + " " * (b - 2) + s)
